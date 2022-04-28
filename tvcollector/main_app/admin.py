from django.contrib import admin
# import your models here
from .models import Tvlist, Studio

# Register your models here
admin.site.register(Tvlist)
admin.site.register(Studio)