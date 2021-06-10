from django.contrib import admin
from .models import Provider

class ProviderAdmin(admin.ModelAdmin):
    #fields =["category","title","description"]
    list_display =["category","title"]
admin.site.register(Provider,ProviderAdmin)
