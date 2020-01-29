# Wagtail CopyableModelAdmin

[![Build Status](https://github.com/cfpb/wagtail-copyablemodeladmin/workflows/test/badge.svg)](https://github.com/cfpb/wagtail-copyablemodeladmin/actions)
[![Coverage Status](https://coveralls.io/repos/github/cfpb/wagtail-copyablemodeladmin/badge.svg?branch=master)](https://coveralls.io/github/cfpb/wagtail-copyablemodeladmin?branch=master)

CopyableModelAdmin is an extension of the [Wagtail ModelAdmin](https://docs.wagtail.io/en/latest/reference/contrib/modeladmin/index.html) that allows for model instances to be copied in the user interface with a "Copy" button.

- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Getting help](#getting-help)
- [Getting involved](#getting-involved)
- [Licensing](#licensing)
- [Credits and references](#credits-and-references)

## Dependencies

- Python 3.6+
- Django 1.11+, 2.0+
- Wagtail 1.13+, 2.0+

## Installation

1. Install wagtail-copyablemodeladmin:

```shell
pip install wagtail-copyablemodeladmin
```

2. Add `copyablemodeladmin` as an installed app in your Django `settings.py`:

 ```python
 INSTALLED_APPS = (
     ...
     'copyablemodeladmin',
     ...
 )
```

## Usage

Please see the [Wagtail ModelAdmin documentation](https://docs.wagtail.io/en/latest/reference/contrib/modeladmin/index.html) for getting started with ModelAdmin. 

When creating a `ModelAdmin` for objects that should be copyable, instead of inheriting from `ModelAdmin`, inherit from `copyablemodeladmin.options.CopyableModelAdmin`:

```python
from wagtail.contrib.modeladmin.options import modeladmin_register
from copyablemodeladmin.options import CopyableModelAdmin
from myapp.models import Book


# Inherit from CopyableModelAdmin instead of ModelAdmin
class BookAdmin(CopyableModelAdmin):
    model = Book
    list_display = ('title', 'author')
    list_filter = ('author',)
    search_fields = ('title', 'author')

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(BookAdmin)
```

In addition to `CopyableModelAdmin`, there are three mixin classes that can be added to other custom `ModelAdmin` subclasses:

```python
from copyablemodeladmin.helpers import CopyButtonHelperMixin
from copyablemodeladmin.options import CopyableModelAdminMixin
from copyablemodeladmin.views import CopyViewMixin


class CustomCopyButtonHelper(CopyButtonHelperMixin, CustomButtonHelper):
    pass


class CustomCopyInstanceView(CopyViewMixin, CustomInstanceSpecificView):
    pass


class CustomCopyableModelAdmin(CopyableModelAdminMixin, ModelAdmin):
    button_helper_class = CustomCopyButtonHelper
    copy_view_class = CustomCopyInstanceView
```


## Getting help

Please add issues to the [issue tracker](https://github.com/cfpb/wagtail-copyablemodeladmin/issues).

## Getting involved

General instructions on _how_ to contribute can be found in [CONTRIBUTING](CONTRIBUTING.md).

## Licensing
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)

## Credits and references

1. Forked from [cfgov-refresh](https://github.com/cfpb/cfgov-refresh)
