from django.contrib import admin
from .models import Pen
from .models import Ink

# Register your models here.
admin.site.register(Pen)
admin.site.register(Ink)