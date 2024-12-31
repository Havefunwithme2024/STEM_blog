from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Q
from .models import Categories, Subjects, Articles, CommentAnonymous, CommentAuthenticated, ViewsArticles, \
    FavoriteArticle, GalleryArticles
from .forms import CommentAnonymousForm, CommentAuthenticatedForm, EditArticleForm, CreateArticleForm
from django.urls import reverse_lazy
from transliterate import translit
from django.utils.text import slugify



# def index_view(request):
#     # QuerySet -> список объектов из БД
#     # Model.objects.all() -> получаем весь QuerySet
#     categories = Categories.objects.all()
#     articles = Articles.objects.all()
#     paginator = Paginator(articles, 3)
#     page = request.GET.get('page')
#     result = paginator.get_page(page)
#
#
#
#     # context -> словарь который будет передавать в шаблоны наш QuerySet
#     context = {
#         'categories': categories,
#         'articles': result,
#         'title': 'Главная Страница'
#     }
#     # render -> функция для отображения шаблона и передачи context
#     return render(request, 'pages/index.html', context)

class IndexView(ListView):
    model = Articles
    context_object_name = 'articles'
    template_name = 'pages/index.html'
    paginate_by = 3
    extra_context = {
          'title': 'Главная страница',
          'categories': Categories.objects.all()
    }


#
#
# def show_category_view(request, pk_cat):
#     categories = Categories.objects.all()
#     # Model.objects.filter(name_filed=parameter) -> получаем QuerySet который подходит по условию
#     articles = Articles.objects.filter(category_id=pk_cat)
#
#     context = {
#         'categories': categories,
#         'articles': articles,
#         'title':f'Категория{pk_cat}'
#     }
#     return render(request, 'pages/index.html', context)

class ShowCategoryView(IndexView):
    def get_query_set(self):
        articles = Articles.objects.filter(category_id=self.kwargs['pk_cat'])
        return articles
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Categories.objects.get(pk=self.kwargs['pk_cat'])
        context['title'] = f'Категория - {category.pk}'
        return context

class SearchArticleView(IndexView):
    def get_queryset(self):
        query = self.request.GET.get('q')
        articles = Articles.objects.filter(
            Q(title__iregex=query) | Q(title__icontains=query)

        )
        return articles
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Результат поиска:'
        return context



#def detail_view(request, slug_article):
    # Model.objects.get(name_field=parameter) -> получаем один объект который подходит по условию
    #article = Articles.objects.get(slug=slug_article)
    # article = get_object_or_404(Articles, slug=slug_article)
    # comment_anonymous = CommentAnonymous.objects.filter(article_id=article.pk)
    # comment_authenticated = CommentAuthenticated.objects.filter(article_id=article.pk)
    # id_article_subject = [art.pk for art in article.subject_article.all()]
    # articles = [Articles.objects.filter(subject_article=art_id) for art_id in id_article_subject]
    #
    # if request.user.is_authenticated:
    #     if not request.session.session_key:
    #         request.session.save()
    #
    #     user_session_key = request.session.session_key
    #     status_view = ViewsArticles.objects.filter(article=article, user_session=user_session_key).exists()
    #     if status_view is False and user_session_key != 'None':
    #         view = ViewsArticles()
    #         view.article = article
    #         view.user_session = user_session_key
    #         view.save()
    #         article.quantity_views += 1
    #         article.save()


    # context = {
    #     'article': article,
    #     'articles':articles[0],
    #     'form_comment_anonymous': CommentAnonymousForm,
    #     'comment_anonymous': comment_anonymous,
    #     'form_comment_authentication': CommentAuthenticatedForm,
    #     'comment_authentication': comment_authenticated,
    #     'title': f'Статья: {article.title}'
    # }
    # return render(request, 'pages/detail.html', context)

class ShowDetailView(DetailView):
    model = Articles
    context_object_name = 'article'
    slug_url_kwarg = 'slug_article'
    template_name='pages/detail.html'
    extra_context = {
        'form_comment_anonymous': CommentAnonymousForm,
        'form_comment_authentication': CommentAuthenticatedForm
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = get_object_or_404(Articles, slug=self.kwargs['slug_article'])
        if self.request.user.is_authenticated:
            if not self.request.session.session_key:
                self.request.session.save()

            user_session_key = self.request.session.session_key
            status_view = ViewsArticles.objects.filter(article=article, user_session=user_session_key).exists()
            if status_view is False and user_session_key != 'None':
                view = ViewsArticles()
                view.article = article
                view.user_session = user_session_key
                view.save()
                article.quantity_views += 1
                article.save()
        id_article_subject = [art.pk for art in article.subject_article.all()]
        articles = [Articles.objects.filter(subject_article=art_id) for art_id in id_article_subject]
        context['articles'] = articles[0]
        context['comment_anonymous']= CommentAnonymous.objects.filter(article_id=article.pk)
        context['comment_authenticated'] = CommentAuthenticated.objects.filter(article_id=article.pk)
        return context



def create_comment_anonymous(request, pk_article):
    form = CommentAnonymousForm(data=request.POST)
    article = Articles.objects.get(pk=pk_article)

    if form.is_valid():
        data_form = form.cleaned_data
        comment = CommentAnonymous.objects.create(name=data_form['name'], content=data_form['content'], article_id=pk_article)
        comment.save()
        return redirect('detail_page', article.slug)



def create_comment_authenticated(request, pk_article):
    form = CommentAuthenticatedForm(data=request.POST)
    article = Articles.objects.get(pk=pk_article)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.article = article

        comment.save()
        return redirect('detail_page', article.slug)

def favorite_logic(request, pk_article):
       user_id = request.user.pk
       status_favorite = FavoriteArticle.objects.filter(author_id=user_id, article_id=pk_article).exists()

       if status_favorite is False:
           favorite = FavoriteArticle.objects.create(author_id=user_id, article_id=pk_article)
           favorite.save()
       else:
           favorite = FavoriteArticle.objects.get(author_id=user_id, article_id=pk_article)
           favorite.delete()

       return redirect(request.META.get('HTTP_REFERER', 'index_page'))

def favorite_view(request):
    favorite = FavoriteArticle.objects.filter(author=request.user)

    context = {
        'favorite': favorite,
        'title': 'Фавориты'
    }
    return render(request, 'pages/favorite.html', context)

class EditArticleView(UpdateView):
    model = Articles
    form_class = EditArticleForm
    template_name = 'pages/edit_article.html'
    extra_context = {
        'title': 'Изменение статьи'
    }
    def get_success_url(self):
        return reverse_lazy('index_page')

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs['pk_article'])

class CreateArticleView(CreateView):
    model = Articles
    form_class = CreateArticleForm
    template_name = 'pages/create_article.html'
    extra_context = {
        'title': 'Создание статьи'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user

        step_first = translit(form.instance.title, reversed=True)
        step_second = slugify(step_first)
        form.instance.slug = self.get_unique_slug(step_second)
        response = super().form_valid(form)
        if 'image' in self.request.FILES:
            images = self.request.FILES.getlist('image')
            for img in images:
                GalleryArticles.objects.create(image=img, article=form.instance)
        return response

    def get_unique_slug(self, slug):
        unique_slug = slug
        num = 1
        while Articles.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug} - {num}'
            num +=1
        return unique_slug



    def get_success_url(self):
        return reverse_lazy('index_page')

def delete_article(request, pk_article):
    article = get_object_or_404(Articles, pk=pk_article)
    article.delete()
    return redirect(request.META.get('HTTP_REFERER', 'index_page'))











