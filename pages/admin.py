from django.contrib import admin
from .models import Categories, Subjects, Articles, GalleryArticles
from django.utils.html import format_html

# простое подключения, плюс: быстрое подключать, минус: нельзя настроить под себя
admin.site.register(Categories)
admin.site.register(Subjects)

# TabularInline -> класс для добавления нескольких объектов
class GalleryArticleInline(admin.TabularInline):
    # указываем модель
    model = GalleryArticles
    # сколько будет по умолчанию объектов
    extra = 1

@admin.register(Articles)
class ArticleAdmin(admin.ModelAdmin):
    # указываем какие отображать поля
    list_display = ['pk', 'title', 'quantity_views', 'is_published', 'is_banned', 'creation_datetime', 'updates_datetime', 'author', 'show_photo']
    # указываем какие поля будут кликабельными
    list_display_links = ['pk', 'title']
    # нужно что-бы поля slug было таким же как title
    prepopulated_fields = {'slug': ['title']}
    # указываем классы Inline
    inlines = [GalleryArticleInline]
    list_per_page = 4
    list_filter = ['category__name', 'subject_article__name']
    search_fields = ['fields']
    ordering = ['pk']
    list_editable = ['is_banned']
    filter_horizontal = ['subject_article']

    @admin.action(description='Фото')
    def show_photo(self, obj):
        try:
            image = obj.get_first_photo()
            return format_html(f'<img src={image} width=100>')
        except:
            return '-'



