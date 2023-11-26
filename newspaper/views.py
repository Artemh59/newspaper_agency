from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

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


class TopicCreateViews(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic")


class TopicDetailViews(generic.DetailView):
    model = Topic
