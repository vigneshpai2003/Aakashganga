from django.contrib.auth.models import User
from aakashvani.models import Page


def init():
    User.objects.create_superuser('admin', 'vignesh.m_pai@students.iiserpune.ac.in', 'vignesh123')
    # root = Page.objects.get(title='Root')
    default = Page.objects.get(title='Welcome to your new Wagtail site!')
    default.delete()
