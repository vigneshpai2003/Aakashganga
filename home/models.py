from email.mime import image
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class Announcement(models.Model):
    header = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    btn = models.CharField(max_length=20)
    link = models.CharField(max_length=200)


class Event(Page):
    priority = models.IntegerField(default=1)
    body = RichTextField(blank=True)
    image = models.URLField(blank=True)
    isVideo = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('priority'),
        FieldPanel('body', classname="full"),
        FieldPanel('image'),
        FieldPanel('isVideo'),
    ]

    subpage_types = []
