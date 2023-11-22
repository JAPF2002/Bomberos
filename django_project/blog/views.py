
from django.views.generic.base import TemplateView

class BlogPageView(TemplateView):
    template_name = "blog.html"