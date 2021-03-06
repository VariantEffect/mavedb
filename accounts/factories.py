"""
accounts.factories
=================

This module contains factory methods for creating test fixtures for
:class:`User` and :class:`Profile`. If there are
any updates to the models which will have an impact on the tests, then they
can be changed once here instead of throughout all the tests. This will help
with future maintainability.
"""

import factory.fuzzy
import factory.faker

from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser


def AnonymousUserFactory():
    """
    Create an anonymous user from :class:`AnonymousUser`.
    """
    return AnonymousUser()


def UserFactory(
    username=None,
    password=None,
    first_name=None,
    last_name=None,
    email=None,
    **kwargs
):
    """
    Test fixture factory for the user class which sets username,
    first_name, last_name and password.
    """
    if email is None:
        email = factory.faker.Faker("email").generate({})
    if username is None:
        username = factory.fuzzy.FuzzyText(length=8).fuzz()
    if password is None:
        password = factory.fuzzy.FuzzyText(length=16).fuzz()

    if User.objects.filter(username=username).count():
        return User.objects.filter(username=username).first()

    name = factory.faker.Faker("name").generate({}).split(" ")
    if first_name is None:
        first_name = name[0]
    if last_name is None:
        last_name = name[-1]

    user = User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        **kwargs
    )
    user.set_password(password)
    return user
