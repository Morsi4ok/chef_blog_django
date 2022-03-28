from django.views.generic import ListView, DetailView, CreateView

from .models import Post, Comment
from .forms import CommentForm


class HomeView(ListView):
    model = Post
    paginate_by = 9  # сколько будем выводить постов на страницу
    template_name = "blog/home.html"  # указываем путь к шаблону


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related(
            'category')  # идём в модели "категории" к полю "слаг" и получаем "слаг"(который указан в "юрл"),фильтрация постов по определённой категории|select_related экономит запросы в БД, добавляет join к запросу и за один запрос выкачивает больше данных(вместо 2-ух запросов выкачивает за 1)


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"  # как будет именоваться наш объект в шаблоне
    slug_url_kwarg = 'post_slug'  # по умолчанию искал бы просто "слаг", а так как переименовали, то надо его переопределить

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):  # URL-адрес для перенаправления после успешной обработки формы.
        return self.object.post.get_absolute_url()
