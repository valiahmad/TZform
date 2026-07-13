import jdatetime
from django import template

register = template.Library()


@register.filter
def shamsi(value):
    """
    Convert a Gregorian date to Jalali (Shamsi).
    """
    if not value:
        return ""

    return jdatetime.date.fromgregorian(date=value).strftime("%Y/%m/%d")