from django.contrib import admin
from .models import CustomUser, ContactUs

from import_export.admin import ImportExportModelAdmin

class USER_IE(ImportExportModelAdmin, admin.ModelAdmin):
    pass
admin.site.register(CustomUser, USER_IE)
admin.site.register(ContactUs)
