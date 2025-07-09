from django.contrib import admin
from . import models
from import_export.admin import ImportExportModelAdmin


class Equipment2Admin(ImportExportModelAdmin):
        ...

admin.site.register(models.Equipment2, Equipment2Admin)

admin.site.site_url = "/mhadatabase/main"

admin.site.site_header = 'MHC Bidding Dashboard'
