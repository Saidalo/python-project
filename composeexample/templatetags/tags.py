import random
from django import template

register = template.Library()


@register.simple_tag
def random_class():
    classes = ['',
               'list-group-item-primary',
               'list-group-item-secondary',
               'list-group-item-success',
               'list-group-item-danger',
               'list-group-item-warning',
               'list-group-item-info',
               'list-group-item-light',
               'list-group-item-dark'
               ]

    return random.choice(classes)
