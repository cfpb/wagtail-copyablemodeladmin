from wagtail.contrib.modeladmin.options import modeladmin_register

from copyablemodeladmin.options import CopyableModelAdmin
from copyablemodeladmin.tests.copyabletestapp.models import Author


@modeladmin_register
class AuthorModelAdmin(CopyableModelAdmin):
    model = Author
    menu_label = 'Author'
    menu_icon = 'user'
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )

    def copy(self, instance):
        new_instance = instance
        new_instance.pk = None
        new_instance.save()
        return new_instance
