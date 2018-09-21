from django import template
from complaints.models import Complaint
import time

register = template.Library()


@register.simple_tag
def not_finished(user):
    return Complaint.objects.nofinished().filter(user__username=user).count()

@register.simple_tag
def title_contain(keyword):
    return Complaint.objects.this_year().filter(title__contains=keyword).count()


@register.simple_tag
def category(pk):
    return Complaint.objects.filter(category=pk).count()


@register.simple_tag
def history_count(pk):
    return Complaint.objects.this_year().filter(category=pk).count()


@register.filter
def counter(value, page):
    pagesize = 10
    return (page - 1) * pagesize + value