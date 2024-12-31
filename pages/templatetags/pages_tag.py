from django import template
from pages.models import FavoriteArticle

register = template.Library()

@register.simple_tag()
def check_favorite_status(article_id, user_id):
    return FavoriteArticle.objects.filter(article_id=article_id, author_id=user_id).exists()
