from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.search import index


class Aakashvani(Page):
    max_count = 1

    subpage_types = ['aakashvani.IndexPage', 'aakashvani.BlogTagIndexPage']

    content_panels = Page.content_panels

    def get_context(self, request):
        context = super().get_context(request)
        context['indexPages'] = sorted(self.get_children().type(IndexPage).live(), key=lambda x: x.specific.priority, reverse=True)
        return context


class IndexPage(Page):
    intro = RichTextField(blank=True)
    priority = models.IntegerField(default=1)

    parent_page_types = ['aakashvani.Aakashvani']

    subpage_types = ['aakashvani.Blog']

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context['blogpages'] = self.get_children().live().order_by('-first_published_at')
        return context


class BlogTag(TaggedItemBase):
    content_object = ParentalKey(
        'Blog',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogTagIndexPage(Page):
    max_count = 1

    parent_page_types = ['aakashvani.Aakashvani']

    subpage_types = []


    def get_context(self, request):
        context = super().get_context(request)
        context['blogpages'] = Blog.objects.filter(tags__name=request.GET.get('tag'))
        return context


class Blog(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogTag, blank=True)

    parent_page_types = ['aakashvani.IndexPage']

    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]
