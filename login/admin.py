from django.contrib import admin
from .models import Executive
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Executive)

class myclass(ImportExportModelAdmin):
    pass