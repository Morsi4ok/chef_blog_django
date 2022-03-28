from django import template
from contact.models import Social, About

register = template.Library()  # Библиотека тегов должна содержать переменную register равную экземпляру django.template.Library, в которой регистрируются все определенные теги и фильтры.


@register.simple_tag()  # просто забирает какую-либо информацию откуда-либо, просто передаёт контекст в шаблон, где мы вызовем этот тег
def get_social_links():  # Вывод ссылок социальных сетей
    return Social.objects.all()


@register.simple_tag()  # просто забирает какую-либо информацию откуда-либо, просто передаёт контекст в шаблон, где мы вызовем этот тег
def get_about():  # Вывод "о нас" (about)
    return About.objects.last()
