"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.utils.translation import gettext_lazy as _

from core import models
from carpark.models import CarPark


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


class CarParkResource(resources.ModelResource):
    class Meta:
        model = CarPark
        import_id_fields = ('park_name',)
        fields = ('park_name', 'location_name', 'park_type_id', 'park_type_desc',
                  'capacity_of_park', 'working_time', 'county_name', 'location')


class CarParkAdmin(ImportExportModelAdmin):
    resource_class = CarParkResource
    list_display = ('park_name', 'location_name', 'park_type_id',
                    'capacity_of_park', 'county_name', 'working_time')
    search_fields = ('park_name', 'location_name',
                     'county_name')

    list_filter = ('park_type_id', 'county_name')


admin.site.register(models.User, UserAdmin)
admin.site.register(CarPark, CarParkAdmin)
