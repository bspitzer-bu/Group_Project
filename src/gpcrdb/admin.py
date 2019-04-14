from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from . import models


class GpcrAdmin(ImportExportModelAdmin):
    pass


class LigandAdmin(ImportExportModelAdmin):
    pass


class BindsRelationshipInline(admin.TabularInline):
    model = models.Binds
    extra = 1


admin.site.register(models.Gpcr, GpcrAdmin)
admin.site.register(models.Ligand, LigandAdmin)
admin.site.register(models.Similarities)
