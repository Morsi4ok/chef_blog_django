from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):  # позволяет делать вложености категорий и если нам нужна структура дерева
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(  # собственно само "дерево"
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):  # метод, который возвращает имя нашей категории
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):  # будет в админке при создании выводится не одинаковое с (1,2,3...), а то, как мы и назвали
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts",
                               on_delete=models.CASCADE)  # привязываем автора, но если удаляется автор, то удаляются все его статьи
    title = models.CharField(max_length=200)  # название для статей
    image = models.ImageField(upload_to='articles/')  # upload_to - куда будет загружаться
    text = models.TextField()  # сам текст или рецепта, не указываем длину, дабы дать расписать как хочет
    category = models.ForeignKey(
        Category,
        related_name="post",
        on_delete=models.SET_NULL,
        null=True
    )  # используем ForeignKey так как у одной категории может быть несколько статей, on_delete=models.SET_NULL чтобы при удалении категории не удалялась сама статья
    tags = models.ManyToManyField(Tag, related_name="post")
    create_at = models.DateTimeField(auto_now_add=True)  # время создания поста, auto_now_add сама ставит нынешнюю дату
    slug = models.SlugField(max_length=200, default="",
                            unique=True)  # поле должно быть уникальным, то чтобы у 2-ух постов не было одинаковых слагов, иначе крашнется)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_single", kwargs={"slug": self.category.slug, "post_slug": self.slug})

    def get_recipes(self):
        return self.recipes.all()

    def get_comments(self):
        return self.comment.all()


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)  # положительные цифры только
    cook_time = models.PositiveIntegerField(default=0)  # положительные цифры только
    ingredients = RichTextField()  # редактор текста(в админке можно увидеть)
    directions = RichTextField()  # редактор текста(в админке можно увидеть)
    post = models.ForeignKey(
        # используем ForeignKey так как у одной статьи может быть несколько рецептов, on_delete=models.SET_NULL чтобы при удалении статьи не удалялась сам рецепт
        Post,
        related_name="recipes",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=150, blank=True, null=True)
    message = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name="comment",
                             on_delete=models.CASCADE)  # удаляя пост, мы удаляем все комментарии
    create_at = models.DateTimeField(auto_now_add=True)  # время создания поста, auto_now_add сама ставит нынешнюю дату
