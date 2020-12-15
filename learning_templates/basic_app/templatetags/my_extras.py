from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value: str, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, "")

# register.filter("cut", cut)