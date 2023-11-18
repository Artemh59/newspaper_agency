from django.views import generic

from newspaper.models import Newspaper


class Index(generic.ListView):
    model = Newspaper
    template_name = "newspaper/index.html"


class About(generic.ListView):
    model = Newspaper
    template_name = "newspaper/about_us.html"
