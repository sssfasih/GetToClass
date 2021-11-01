from django.contrib import admin
from .models import User, UserImage
# Register your models here.


admin.site.register(UserImage)

class UserImageInline(admin.TabularInline):
    model = UserImage
    extra = 3

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ UserImageInline, ]

admin.site.register(User, PropertyAdmin)