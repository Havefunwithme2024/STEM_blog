from django.template import Library

register = Library()

@register.simple_tag()
def transform_text(value):
    if value is True:
        return 'Да'
    elif value is False:
        return 'Нет'



