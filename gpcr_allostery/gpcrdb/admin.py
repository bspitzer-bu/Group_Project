from django.contrib import admin

from . import models


class BindsRelationshipInline(admin.TabularInline):
    model = models.Binds
    extra = 1


class GpcrAdmin(admin.ModelAdmin):
    inlines = (BindsRelationshipInline,)


class LigandAdmin(admin.ModelAdmin):
    inlines = (BindsRelationshipInline,)


admin.site.register(models.Gpcr, GpcrAdmin)
admin.site.register(models.Ligand, LigandAdmin)
