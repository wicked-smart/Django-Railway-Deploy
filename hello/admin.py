from django.contrib import admin
from .models import User, Airport, Flight
# Register your models here.

admin.site.register(User)
admin.site.register(Airport)
admin.site.register(Flight)
