from django.contrib import admin
from .models import Feedback

from import_export.admin import ImportExportModelAdmin
# Register your models here.


class myclass(ImportExportModelAdmin):
    pass



admin.site.register(Feedback)