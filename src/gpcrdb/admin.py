from django.contrib import admin

from . import models


class BindsRelationshipInline(admin.TabularInline):
    model = models.Binds
    extra = 1

# This is how to make inlines with the foreign keys referencing the same model
# class Sims1RelationshipInline(admin.TabularInline):
#     model = models.Similarities
#     fk_name = 'gpcr1'
#
# class Sims2RelationshipInline(admin.TabularInline):
#     model = models.Similarities
#     fk_name = 'gpcr2'


class GpcrAdmin(admin.ModelAdmin):
    inlines = (BindsRelationshipInline,)


class LigandAdmin(admin.ModelAdmin):
    inlines = (BindsRelationshipInline,)


admin.site.register(models.Gpcr, GpcrAdmin)
admin.site.register(models.Ligand, LigandAdmin)
admin.site.register(models.Similarities)
