from django.views import generic

from newspaper.models import Newspaper, Topic, Redactor


class Index(generic.TemplateView):
    template_name = "newspaper/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topics"] = Topic.objects.count()
        context["news"] = Newspaper.objects.count()
        context["redactors"] = Redactor.objects.count()
        return context


class AboutUsView(generic.ListView):
    model = Newspaper
    template_name = "newspaper/about_us.html"


class TopicViews(generic.ListView):
    model = Topic


class TopicDetailViews(generic.DetailView):
    model = Topic
