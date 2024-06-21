from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test, login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import redirect


def superuser_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='admin_login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def supervisor_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='admin_login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_supervisor or u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


def staff_member_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='admin_login'):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator


class StaffRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(
                request,
                'You do not have the permission required to perform the '
                'requested operation.')
            return redirect('home')
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class SuperUserRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(
                request,
                'You do not have the permission required to perform the '
                'requested operation.')
            return redirect('home')
        return super(SuperUserRequiredMixin, self).dispatch(request, *args, **kwargs)
