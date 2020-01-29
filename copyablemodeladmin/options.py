from __future__ import unicode_literals

from django.conf.urls import url

from wagtail.contrib.modeladmin.options import ModelAdmin

from copyablemodeladmin.helpers import CopyButtonHelper
from copyablemodeladmin.views import CopyInstanceView


class CopyableModelAdminMixin:
    button_helper_class = CopyButtonHelper
    copy_view_class = CopyInstanceView

    def copy(self, instance):
        raise NotImplementedError(
            "The copy() method must be implemented for each model admin"
        )  # pragma: no cover

    def copy_view(self, request, instance_pk):
        return self.copy_view_class.as_view(
            model_admin=self, instance_pk=instance_pk
        )(request)

    def get_admin_urls_for_registration(self, parent=None):
        urls = super().get_admin_urls_for_registration()

        # Add the copy URL
        urls = urls + (
            url(
                self.url_helper.get_action_url_pattern('copy'),
                self.copy_view,
                name=self.url_helper.get_action_url_name('copy')
            ),
        )

        return urls


class CopyableModelAdmin(CopyableModelAdminMixin, ModelAdmin):
    pass
