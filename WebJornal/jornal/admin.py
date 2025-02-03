from django.contrib import admin
from .models import Subject, EducationalMaterial


@admin.register(EducationalMaterial)
class EducationalMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject')
    list_filter = ('subject',)


admin.site.register(Subject)
