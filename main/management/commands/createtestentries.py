import sys

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import transaction

from accounts.factories import UserFactory
from accounts.permissions import assign_user_as_instance_admin

from metadata.models import (
    UniprotOffset, RefseqOffset, EnsemblOffset
)

from dataset.factories import ExperimentWithScoresetFactory
from variant.factories import VariantFactory


User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('clear', nargs='?', type=bool, default=False)

    def handle(self, *args, **kwargs):
        password = "1234qwer"
        with transaction.atomic():
            for i, username in enumerate(['usera', 'userb', 'userc', 'userd']):
                user = UserFactory(username=username)
                user.set_password(password)
                user.save()
                for publish in [False, True]:
                    instance = ExperimentWithScoresetFactory()
                    for scoreset in instance.children.all():
                        UniprotOffset.objects.create(
                            offset=i*3 + 1,
                            target=scoreset.target,
                            identifier=scoreset.target.uniprot_id
                        )
                        RefseqOffset.objects.create(
                            offset=i*3 + 2,
                            target=scoreset.target,
                            identifier=scoreset.target.refseq_id
                        )
                        EnsemblOffset.objects.create(
                            offset=i*3 + 3,
                            target=scoreset.target,
                            identifier=scoreset.target.ensembl_id
                        )
                        
                        if publish:
                            scoreset.publish()
                        
                        scoreset.set_modified_by(user, propagate=True)
                        scoreset.set_created_by(user, propagate=True)
                        for i in range(10):
                            VariantFactory(scoreset=scoreset)
                        scoreset.save(save_parents=True)
    
                        scoreset.add_administrators(user)
                        scoreset.experiment.add_administrators(user)
                        scoreset.experiment.experimentset.add_administrators(user)

                sys.stdout.write("Created {}\n".format(instance.urn))