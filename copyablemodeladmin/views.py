from __future__ import unicode_literals

from django.contrib.admin.utils import quote
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

from wagtail.contrib.modeladmin.views import InstanceSpecificView


class CopyViewMixin:

    @method_decorator(login_required)
    def dispatch(self, request, *arg, **kwargs):
        new_instance = self.model_admin.copy(self.instance)
        return redirect(
            self.url_helper.get_action_url('edit', quote(new_instance.pk))
        )


class CopyInstanceView(CopyViewMixin, InstanceSpecificView):
    pass
