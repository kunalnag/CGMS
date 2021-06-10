from django.contrib import admin
from .models import *
from .models import Product
from import_export.admin import ImportExportModelAdmin

@admin.register(Ticket)
@admin.register(Priority)
@admin.register(Status)
@admin.register(Source)
@admin.register(Product)

class myclass(ImportExportModelAdmin):
    pass