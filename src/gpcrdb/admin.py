from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from . import models


class BindsRelationshipInline(admin.TabularInline):
    model = models.Binds
    extra = 1


class GpcrAdmin(ImportExportModelAdmin):
    inlines = (BindsRelationshipInline,)


class LigandAdmin(ImportExportModelAdmin):
    inlines = (BindsRelationshipInline,)


class SimilaritiesAdmin(ImportExportModelAdmin):
    pass


class BindsAdmin(ImportExportModelAdmin):
    pass


admin.site.register(models.Gpcr, GpcrAdmin)
admin.site.register(models.Ligand, LigandAdmin)
admin.site.register(models.Similarities, SimilaritiesAdmin)
admin.site.register(models.Binds, BindsAdmin)
