from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """

    return value.replace(arg, '')

# first param kay maoy name magamit sa template filtering ang second kay ang function mismo
# register.filter('cut', cut)
