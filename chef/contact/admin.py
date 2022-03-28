from django.contrib import admin
from .models import ContactModel, ContactLink, About, Social, ImageAbout


class ImageAboutInline(admin.StackedInline):  # позволяет редактировать связанные объекты
    model = ImageAbout
    extra = 1  # сразу открыто для заполнения только 1 рецепт( но можно добавлять больше)


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "create_at"]  # указывает какие поля отображать на странице списка объектов
    list_display_links = (
    "name",)  # указывает какие поля в list_display будут ссылками на страницу редактирования объекта


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ImageAboutInline]  # сразу при создании можем добавить изображение


admin.site.register(ContactLink)
admin.site.register(Social)
