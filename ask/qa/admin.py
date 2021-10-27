from django.contrib import admin

from .models import *

admin.site.register(Answer)
admin.site.register(Ip)


@admin.register(Question)
class PostAdmin(admin.ModelAdmin):
    pass
