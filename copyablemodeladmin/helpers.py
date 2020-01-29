from __future__ import unicode_literals

from django.contrib.admin.utils import quote

from wagtail.contrib.modeladmin.helpers import ButtonHelper


class CopyButtonHelperMixin:

    def copy_button(self, pk):
        cn = 'button button-small button-secondary'
        return {
            'url': self.url_helper.get_action_url('copy', quote(pk)),
            'label': 'Copy',
            'classname': cn,
            'title': 'Copy this {}'.format(self.verbose_name),
        }

    def get_buttons_for_obj(self, obj, exclude=None, classnames_add=None,
                            classnames_exclude=None):
        if exclude is None:
            exclude = []

        usr = self.request.user
        ph = self.permission_helper
        pk = getattr(obj, self.opts.pk.attname)

        btns = super().get_buttons_for_obj(
            obj,
            exclude=exclude,
            classnames_add=classnames_add,
            classnames_exclude=classnames_exclude
        )

        # Use the edit permission to double for copying
        if('copy' not in exclude and ph.user_can_edit_obj(usr, obj)):
            btns.insert(
                -1,
                self.copy_button(pk)
            )

        return btns


class CopyButtonHelper(CopyButtonHelperMixin, ButtonHelper):
    pass
