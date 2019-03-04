from django.contrib import admin
from .models import User, Category, Location, tags, Pics


class PicsAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)
# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(tags)
admin.site.register(Pics,PicsAdmin)
