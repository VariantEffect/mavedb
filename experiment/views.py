from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView
from django.forms import formset_factory
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from accounts.permissions import (
    assign_user_as_instance_admin, PermissionTypes
)

from main.utils.versioning import save_and_create_revision_if_tracked_changed
from main.fields import ModelSelectMultipleField as msmf
from main.forms import (
    KeywordForm, ExternalAccessionForm,
    ReferenceMappingForm, TargetOrganismForm
)
from main.models import (
    Keyword, ExternalAccession,
    TargetOrganism, ReferenceMapping
)

from scoreset.views import scoreset_create_view

from .models import Experiment, ExperimentSet
from .forms import ExperimentForm


ReferenceMappingFormSet = formset_factory(ReferenceMappingForm)
REFERENCE_MAPPING_FORM_PREFIX = "reference_mapping"


class ExperimentDetailView(DetailView):
    """
    object in question and render a simple template for public viewing, or
    Simple class-based detail view for an `Experiment`. Will either find the
    404.

    Parameters
    ----------
    accession : `str`
        The accession of the `Experiment` to render.
    """
    model = Experiment
    template_name = 'experiment/experiment.html'
    context_object_name = "experiment"

    def dispatch(self, request, *args, **kwargs):
        try:
            experiment = self.get_object()
        except Http404:
            response = render(
                request=request,
                template_name="main/404_not_found.html"
            )
            response.status_code = 404
            return response

        has_permission = self.request.user.has_perm(
            PermissionTypes.CAN_VIEW, experiment)
        if experiment.private and not has_permission:
            response = render(
                request=request,
                template_name="main/403_forbidden.html",
                context={"instance": experiment},
            )
            response.status_code = 403
            return response
        else:
            return super(ExperimentDetailView, self).dispatch(
                request, *args, **kwargs
            )

    def get_object(self):
        accession = self.kwargs.get('accession', None)
        return get_object_or_404(Experiment, accession=accession)


class ExperimentSetDetailView(DetailView):
    """
    Simple class-based detail view for an `ExperimentSet`. Will either find the
    object in question and render a simple template for public viewing, or
    404.

    Parameters
    ----------
    accession : `str`
        The accession of the `ExperimentSet` to render.
    """
    model = ExperimentSet
    template_name = 'experiment/experimentset.html'
    context_object_name = "experimentset"

    def dispatch(self, request, *args, **kwargs):
        try:
            experimentset = self.get_object()
        except Http404:
            response = render(
                request=request,
                template_name="main/404_not_found.html"
            )
            response.status_code = 404
            return response

        has_permission = self.request.user.has_perm(
            PermissionTypes.CAN_VIEW, experimentset)
        if experimentset.private and not has_permission:
            response = render(
                request=request,
                template_name="main/403_forbidden.html",
                context={"instance": experimentset},
            )
            response.status_code = 403
            return response
        else:
            return super(ExperimentSetDetailView, self).dispatch(
                request, *args, **kwargs
            )

    def get_object(self):
        accession = self.kwargs.get('accession', None)
        return get_object_or_404(ExperimentSet, accession=accession)


def parse_mapping_formset(reference_mapping_formset):
    """
    Parses a `ReferenceMappingFormSet` into a list of non-commited
    `ReferenceMapping` models. If the form is not valid for a particular
    form, then `None` is appended to the list.

    Parameters
    ----------
    reference_mapping_formset : `ReferenceMappingFormSet`
        A bound ReferenceMappingFormSet instance.

    Returns
    -------
    `list`
        A list of instantiated models, but non-commited.
    """
    objects = []
    for i, form in enumerate(reference_mapping_formset):
        if form.is_valid():
            if form.cleaned_data:
                model = form.save(commit=False)
                objects.append(model)
        else:
            objects.append(None)
    return objects


@login_required(login_url=reverse_lazy("accounts:login"))
def experiment_create_view(request):
    """
    This view serves up four types of forms:
        - `ExperimentForm` for the instantiation of an Experiment instnace.
        - `ReferenceMappingFormSet` for the instantiation and linking of M2M
          `ReferenceMapping` instnaces.

    A new experiment instance will only be created if all forms pass validation
    otherwise the forms with the appropriate errors will be served back. Upon
    success, the user is redirected to the newly created experiment page.

    Parameters
    ----------
    request : `object`
        The request object that django passes into all views.
    """
    context = {}
    pks = [i.pk for i in request.user.profile.administrator_experimentsets()]
    experimentsets = ExperimentSet.objects.filter(
        pk__in=set(pks)
    ).order_by("accession")

    experiment_form = ExperimentForm()
    experiment_form.fields["experimentset"].queryset = experimentsets
    ref_mapping_formset = ReferenceMappingFormSet(
        prefix=REFERENCE_MAPPING_FORM_PREFIX
    )
    context["experiment_form"] = experiment_form
    context["reference_mapping_formset"] = ref_mapping_formset

    # If you change the prefix arguments here, make sure to change them
    # in the corresponding template element id fields as well. If you don't,
    # expect everything to break horribly. You've been warned.
    if request.method == "POST":

        # Get the new keywords/accession/target org so that we can return
        # them for list repopulation if the form has errors.
        keywords = request.POST.getlist("keywords")
        keywords = [kw for kw in keywords if msmf.is_word(kw)]
        e_accessions = request.POST.getlist("external_accessions")
        e_accessions = [ea for ea in e_accessions if msmf.is_word(ea)]
        target_organism = request.POST.getlist("target_organism")
        target_organism = [to for to in target_organism if msmf.is_word(to)]

        experiment_form = ExperimentForm(request.POST)
        experiment_form.fields["experimentset"].queryset = experimentsets
        ref_mapping_formset = ReferenceMappingFormSet(
            request.POST, prefix=REFERENCE_MAPPING_FORM_PREFIX
        )
        context["experiment_form"] = experiment_form
        context["reference_mapping_formset"] = ref_mapping_formset
        context["repop_keywords"] = ','.join(keywords)
        context["repop_external_accessions"] = ','.join(e_accessions)
        context["repop_target_organism"] = ','.join(target_organism)

        maps = parse_mapping_formset(ref_mapping_formset)
        if not all([m is not None for m in maps]) or \
                not experiment_form.is_valid():
            return render(
                request,
                "experiment/new_experiment.html",
                context=context
            )

        experiment = experiment_form.save(commit=True)
        for ref_map in maps:
            ref_map.experiment = experiment
            ref_map.save()

        # Save and update permissions. If no experimentset was selected,
        # by default a new experimentset is created with the current user
        # as it's administrator.
        user = request.user
        assign_user_as_instance_admin(user, experiment)
        experiment.created_by = user
        experiment.update_last_edit_info(user)
        save_and_create_revision_if_tracked_changed(user, experiment)

        if not request.POST['experimentset']:
            assign_user_as_instance_admin(user, experiment.experimentset)
            experiment.experimentset.update_last_edit_info(user)
            save_and_create_revision_if_tracked_changed(
                user, experiment.experimentset
            )

        return scoreset_create_view(
            request,
            came_from_new_experiment=True,
            e_accession=experiment.accession
        )
    else:
        return render(
            request,
            "experiment/new_experiment.html",
            context=context
        )
