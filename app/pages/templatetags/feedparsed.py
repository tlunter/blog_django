from django.template import Library
import datetime 

register = Library()

@register.filter
def feedparsed(value):
    return datetime.datetime(*value[:6])
