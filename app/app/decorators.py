from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.urlresolvers import reverse

def is_staff(function=None, permission=None, redirect_field_name=REDIRECT_FIELD_NAME):
    actual_decorator = None
    if permission:
        actual_decorator = user_passes_test(
            lambda u: u.is_staff or u.has_perm(permission),
            redirect_field_name=redirect_field_name
        )
                
    if actual_decorator is None:
        actual_decorator = user_passes_test(
            lambda u: u.is_staff,
            redirect_field_name=redirect_field_name
        )
    
    if function:
        return actual_decorator(function)
    return actual_decorator
