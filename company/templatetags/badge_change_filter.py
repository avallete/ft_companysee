from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(needs_autoescape=True)
def badge_change(value, arg, autoescape=True):
    ivalue = int(value)
    iarg = int(arg)
    if (value > arg):
        result = '<span class="badge badge-success badge-pill">+%d%%</span>' % ((ivalue - iarg) / (iarg/100))
    elif (value < arg):
        result = '<span class="badge badge-danger badge-pill">%d%%</span>' % ((ivalue - iarg) / (iarg/100))
    else:
        result = '<span class="badge badge-info badge-pill">0</span>'
    return mark_safe(result)