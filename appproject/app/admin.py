from django.contrib import admin

# Register your models here.
from app.models import Users
from app.models import Games

admin.site.register(Users)
admin.site.register(Games)

