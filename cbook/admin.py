from django.contrib import admin

# Register your models here.

from .models import Contact
from .models import Address
from .models import Phone
from .models import Date

admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Date)