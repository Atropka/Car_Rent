from django.contrib import admin
from .models import Car, Contact, Review
from django.utils.html import format_html  # Для корректного отображения изображений
from django.db import models

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
    'brand', 'body_type', 'price_per_day', 'image_thumbnail')  # Добавляем функцию для отображения миниатюры изображения
    search_fields = ('brand', 'body_type')
    list_filter = ('brand', 'body_type')
    ordering = ('brand',)

    fields = ('brand', 'body_type', 'price_per_day', 'image')  # Поля, которые будут отображаться в форме
    list_editable = ('price_per_day',)

    # Функция для отображения миниатюры изображения в списке
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{url}" width="50" height="50"/>', url=obj.image.url)
        return "Нет изображения"

    image_thumbnail.short_description = 'Миниатюра'  # Описание колонки

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'message', 'created_at')  # Поля, которые будут отображаться в списке
    search_fields = ('name', 'email')  # Поля, по которым можно искать
    list_filter = ('created_at',)  # Фильтры для удобного поиска

# Регистрируем модель в админке
admin.site.register(Contact, ContactAdmin)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # Показываем имя и дату создания отзыва в списке
    search_fields = ('name', 'message')    # Добавляем возможность поиска по имени и сообщению
    list_filter = ('created_at',)          # Фильтрация по дате