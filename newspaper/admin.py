from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import Redactor, Topic, Newspaper


admin.site.unregister(Group)


@admin.register(Redactor)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("years_of_experience",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "years_of_experience",
                    )
                },
            ),
        )
    )


@admin.register(Topic)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Newspaper)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("title",)
