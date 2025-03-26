from django.contrib import admin
from .models import Contact,test
# Register your models here.

# admin.site.register(Contact)
admin.site.register(test)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
     list_display=["id",'fullname','email','mobile','message']
     search_fields=["fullname",'email']
     list_filter=["fullname",'email']