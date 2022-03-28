from django import template
from blog.models import Category, Post

register = template.Library()  # Библиотека тегов должна содержать переменную register равную экземпляру django.template.Library, в которой регистрируются все определенные теги и фильтры.


def get_all_categories():  # для удобства создал функцию, которая возвращает все категории
    return Category.objects.all()


@register.simple_tag()  # просто забирает какую-либо информацию откуда-либо, просто передаёт контекст в шаблон, где мы вызовем этот тег
def get_list_category():  # Вывод всех категорий
    return get_all_categories()


@register.inclusion_tag(
    'blog/include/tags/top_menu.html')  # рендерит шаблон и в то место, где мы вызовем этот тег - он туда выведет этот готовый отрендеренный html (в основном отличие от симпл, что умеет рендерить) и указываем шаблон, где будет рендерить
def get_categories():  # выводить список категорий
    category = get_all_categories()  # выводим все категории без сортировки
    return {"list_category": category}  # возвращаем словарь


@register.inclusion_tag(
    'blog/include/tags/recipes_tag.html')  # рендерит шаблон и в то место, где мы вызовем этот тег - он туда выведет этот готовый отрендеренный html (в основном отличие от симпл, что умеет рендерить) и указываем шаблон, где будет рендерить
def get_last_posts():  # выводить список категорий
    posts = Post.objects.select_related("category").order_by("-id")[
            :5]  # чтобы лишние запросы в базу не лезли + по id выбираем последние 5 штук
    return {"list_last_post": posts}  # возвращаем словарь
