from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
class Authorissue(admin.ModelAdmin):
    pass

class Authorcomment(admin.ModelAdmin):
    pass
admin.site.register(issue, Authorissue)

admin.site.register(comment, Authorcomment)
