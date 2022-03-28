from django import template
from gallery.models import Photo

register = template.Library()  # Библиотека тегов должна содержать переменную register равную экземпляру django.template.Library, в которой регистрируются все определенные теги и фильтры.


@register.inclusion_tag(
    'blog/include/tags/gallery_tag.html')  # рендерит шаблон и в то место, где мы вызовем этот тег - он туда выведет этот готовый отрендеренный html
def get_gallery():
    photos = Photo.objects.order_by()  # забираем фотографии
    return {"photos": photos}
