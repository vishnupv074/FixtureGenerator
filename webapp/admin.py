from django.contrib import admin
from .models import Teams, Matches, Venues

# Register your models here.
admin.site.register(Teams)
admin.site.register(Matches)
admin.site.register(Venues)