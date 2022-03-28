from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class RecipeInline(admin.StackedInline):  # позволяет редактировать связанные объекты
    model = models.Recipe
    extra = 1  # сразу открыто для заполнения только 1 рецепт( но можно добавлять больше)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "create_at",
                    "id"]  # указывает какие поля отображать на странице списка объектов
    prepopulated_fields = {
        'slug': ('title', 'category'), }  # автозаполнение поля slug, когда заполняем поле title и category
    inlines = [RecipeInline]  # сразу при создании поста можем добавить и рецепт к нему
    save_as = True  # я бы сказал, что для удобства теста работает ли, не создавать с нуля новый пост,а просто уже существующий сохранить как новый объект
    save_on_top = True  # в основном для удобства, чтобы в админке "кнопки" были сверху, а не снизу(дабы не листать вниз)


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time",
                    "post"]  # указывает какие поля отображать на странице списка объектов


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'create_at',
                    'id']  # указывает какие поля отображать на странице списка объектов


admin.site.register(models.Category, MPTTModelAdmin)  # в админке позволяет увидеть какая категория к какой принадлежит
admin.site.register(models.Tag)
