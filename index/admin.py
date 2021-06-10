from django.contrib import admin
from .models import Customer
# Register your models here.
from import_export.admin import ImportExportModelAdmin

@admin.register(Customer)

class myclass(ImportExportModelAdmin):
    pass