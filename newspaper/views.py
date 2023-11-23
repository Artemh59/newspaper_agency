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


class About(generic.ListView):
    model = Newspaper
    template_name = "newspaper/about_us.html"


class TopicViews(generic.ListView):
    model = Topic
    template_name = "newspaper/topics.html"


class NewspaperDetailViews(generic.DetailView):
    model = Topic
    template_name = "newspaper/topic_detail.html"
