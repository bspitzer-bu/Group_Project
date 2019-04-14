from django.contrib import admin
from django import forms
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

class GpcrAdmin(ImportExportModelAdmin):
    pass

from . import models

class BindsRelationshipInline(admin.TabularInline):
    model = models.Binds
    extra = 1

class LigandAdmin(admin.ModelAdmin):
    inlines = (BindsRelationshipInline,)

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

admin.site.register(models.Gpcr, GpcrAdmin)
admin.site.register(models.Ligand, LigandAdmin)
admin.site.register(models.Similarities)
