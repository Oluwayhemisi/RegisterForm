from django.contrib import admin
from .models import Contact


# Register your models here.

admin.site.register(Contact)
list_displayed=['firstname', 'lastname', 'email']
search_fields=['firstname']
firstname_hierarchy= 'firstname'
