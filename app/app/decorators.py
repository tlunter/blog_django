from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.urlresolvers import reverse

def is_staff(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    actual_decorator = user_passes_test(
        lambda u: u.is_staff,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
