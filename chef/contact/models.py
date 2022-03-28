from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):  # Класс модели обратной связи
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)  # необязательное поле для заполнения
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'  # чтобы показывало кто написал


class ContactLink(models.Model):  # Класс модели контактов
    icon = models.FileField(upload_to='icons/')  # куда будет загружаться иконка
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class About(models.Model):  # Класс модели страницы о нас
    name = models.CharField(max_length=50, default='')
    text = RichTextField()  # редактор текста(в админке можно увидеть)
    mini_text = RichTextField()  # редактор текста(в админке можно увидеть)

    def get_first_image(self):  # получить первую картинку
        item = self.about_images.first()
        return item.image.url

    def get_images(self):  # получить картинки после 1-ой
        return self.about_images.order_by('id')[1:]


class ImageAbout(models.Model):  # Класс модели изображений страницы о нас
    image = models.ImageField(upload_to="about/")  # куда будет загружаться картинка
    page = models.ForeignKey(About, on_delete=models.CASCADE, related_name="about_images")  # связь с таблицей about
    alt = models.CharField(max_length=100)


class Social(models.Model):  # Класс модели соц сетей страницы о нас
    icon = models.FileField(upload_to="icons/")  # куда будет загружаться иконка
    name = models.CharField(max_length=200)
    link = models.URLField()  # CharField для URL-адреса
