from django.contrib import admin

from .models import place
from .models import team
from .models import task

# Register your models here.

admin.site.register(place)
admin.site.register(team)
admin.site.register(task)
