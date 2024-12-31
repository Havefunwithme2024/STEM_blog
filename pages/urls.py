from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_page'),
    path('show/category/<int:pk_cat>/', views.ShowCategoryView.as_view(), name='show_category'),
    path('search/articles/', views.SearchArticleView.as_view(), name='search_article_active'),
    path('show/article/<slug:slug_article>/', views.ShowDetailView.as_view(), name='detail_page'),
    path('edit/article/<int:pk_article>/', views.EditArticleView.as_view(), name='edit_article_active'),
    path('create/article/', views.CreateArticleView.as_view(), name='create_article_active'),
    path('delete/article/<int:pk_article>/', views.delete_article, name='delete_article_active'),
    path('save/comment/anonymous/<int:pk_article>/', views.create_comment_anonymous, name='save_comment_anonymous'),
    path('save/comment/authenticated/<int:pk_article>/', views.create_comment_authenticated,
         name='save_comment_authenticated'),
    path('activate/favorite/<int:pk_article>/', views.favorite_logic, name='favorite_active'),
    path('show/favorite/', views.favorite_view, name='favorite_page')


]
