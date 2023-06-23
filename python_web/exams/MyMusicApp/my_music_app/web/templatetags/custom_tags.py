from django import template

from ..models import Profile, Album

register = template.Library()


@register.simple_tag
def get_profile():
    return Profile.objects.first()


@register.simple_tag
def get_albums():
    return Album.objects.all()


@register.simple_tag
def get_album(pk):
    return Album.objects.filter(pk=pk).first()
