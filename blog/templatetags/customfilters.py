from django import template
register = template.Library()

@register.filter(name="parity")
def parity(value):
    if value % 2 != 0:
        return True
    else:
        return False
