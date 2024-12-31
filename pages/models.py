from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator


class Categories(models.Model):
    # CharField -> текстовое поля с ограниченной длиной
    # max_length -> ограничитель
    # verbose_name -> имя поля
    name = models.CharField(max_length=250, verbose_name='Имя категории')

    def __str__(self):
        return self.name

    # мета классы, нужны для изменения свой родительского класса
    class Meta:
        # verbose_name -> имя в единственном числе
        verbose_name = 'Категория'
        # verbose_name_plural -> имя в множественном числе
        verbose_name_plural = 'Категории'


class Subjects(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя тематики')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тематика'
        verbose_name_plural = 'Тематику'

class Articles(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    # IntegerField ->
    # default ->
    quantity_views = models.IntegerField(default=0, verbose_name='Кло-во просмотров')
    # TextField -> текстовое поля не ограниченной длины
    description = models.TextField(verbose_name='Описание')
    card_description = models.TextField(verbose_name='Короткое описание', validators=[

        MinLengthValidator(25),  # MinLengthValidator -> минимальных значений

        MaxLengthValidator(35)  # MaxLengthValidator -> максимальных значений
    ])
    # BooleanField -> поля для булевого типа данных
    # default -> значения по умолчанию
    is_published = models.BooleanField(default=True, verbose_name='Опубликовать')
    is_banned = models.BooleanField(default=False, verbose_name='Заблокированная статья')
    # ForeignKey -> поля для связи ManyToOne
    # on_delete -> что будет с объектом после удаления
    # CASCADE -> при удалении пользователя статья удалиться
    # PROTECT -> не даст удалить пользователя, так как у нее есть статья
    # SET_NULL -> при удалении пользователя, в поле author будет NONE/NULL
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    # DateTimeField -> поля для даты и времени
    # auto_now_add -> заполняет дату_время при создание
    # auto_now -> заполняет дату_время при создание, и меняет время после обновления
    creation_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Время и дата создания')
    updates_datetime = models.DateTimeField(auto_now=True, verbose_name='Время и дата обновления')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Автар статьи')
    # ManyToManyField ->
    subject_article = models.ManyToManyField(Subjects, verbose_name='Тематика статьи')
    timing_article = models.TimeField(auto_now_add=False, verbose_name='Хронометраж статьи')
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.title

    def get_first_photo(self):
        try:
            photo = self.gallery_articles.all().first()
            return photo.image.url
        except Exception as e:
            print(e)
            return 'https://cdn.vectorstock.com/i/500p/46/50/missing-picture-page-for-website-design-or-mobile-vector-27814650.jpg'

    def get_all_photo(self):
        try:
            photo = self.gallery_articles.all()[1:]
            return photo
        except Exception as e:
            print(e)
            return 'https://cdn.vectorstock.com/i/500p/46/50/missing-picture-page-for-website-design-or-mobile-vector-27814650.jpg'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class GalleryArticles(models.Model):
    image = models.ImageField(upload_to='articles/', verbose_name='Фотки')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='gallery_articles')


class CommentAnonymous(models.Model):
    name = models.CharField(max_length=250, verbose_name='Автор комментария')
    content = models.TextField(verbose_name='Описание комментария')
    datetime_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)

class CommentAuthenticated(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария')
    content = models.TextField(verbose_name='Описание комментария')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, verbose_name='Статья')

class ViewsArticles(models.Model):
    article = models.ForeignKey(Articles, on_delete =models.CASCADE)
    user_session = models.CharField(max_length=250)

class FavoriteArticle(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Articles, on_delete=models.CASCADE)