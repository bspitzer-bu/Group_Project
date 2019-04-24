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


class BindsResource(resources.ModelResource):
    pdb_id = fields.Field(
        column_name='pdb_id',
        attribute='pdb_id',
        widget=ForeignKeyWidget(models.Gpcr, 'pdb_id'))

    class Meta:
        model = models.Gpcr

class BindsAdmin(ImportExportModelAdmin):
    resources_class = BindsResource


admin.site.register(models.Gpcr, GpcrAdmin)
admin.site.register(models.Ligand, LigandAdmin)
admin.site.register(models.Similarities, SimilaritiesAdmin)
admin.site.register(models.Binds, BindsAdmin)
