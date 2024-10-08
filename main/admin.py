from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Genders)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('company', 'price', 'category', 'gender', 'image_view')
    list_editable = ('price','category', 'gender')

    def image_view(self, image):
        return mark_safe(f'<img src="{image.image.url}" style="width: 70px;" />')
    image_view.short_description = 'Image'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'product')