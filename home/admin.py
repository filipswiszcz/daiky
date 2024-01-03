from django.contrib import admin

from home.models import (
    Country,
    Language
)


admin.site.register(Country)
admin.site.register(Language)