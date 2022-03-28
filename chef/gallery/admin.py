from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Photo, Gallery


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "get_image")  # указывает какие поля отображать на странице списка объектов
    readonly_fields = ("get_image",)  # отображает только для просмотра или чтения(без возможности редактирования)
    prepopulated_fields = {'slug': ('name',)}  # автозаполнение поля slug, когда заполняем поле name

    def get_image(self, obj):  # сразу видно в админке какая фотография была добавлена для этого объекта
        return mark_safe(
            f'<img src={obj.image.url} width="110" height="80"')  # откуда взять и с каким размером показывать


@admin.register(Gallery)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date")  # указывает какие поля отображать на странице списка объектов
