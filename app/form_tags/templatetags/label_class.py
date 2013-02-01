from django import template

register = template.Library()

@register.filter(is_safe=True)
def label_class(value, arg):

    return value.label_tag(attrs={'class': arg})
