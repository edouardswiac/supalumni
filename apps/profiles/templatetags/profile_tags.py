from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def get_picture_url(id_booster):
    return "http://www.campus-booster.net/actorpictures/"+id_booster+".jpg"

@register.filter
def get_company_flag(h, key):
    obj = h.get(key, "")
    if obj:
        return obj.get('company_flag', "")
    return obj

@register.filter
def get_company_name(h, key):
    obj = h.get(key, "")
    if obj:
        return obj.get('company_name', "")
    return obj