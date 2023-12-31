from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from newspaper.forms import NewForm
from newspaper.models import Newspaper, Topic, Redactor
from newspaper.forms import SignUpForm


class Index(generic.TemplateView):
    template_name = "newspaper/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topics"] = Topic.objects.count()
        context["news"] = Newspaper.objects.count()
        context["redactors"] = Redactor.objects.count()
        return context


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


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


class TopicDeleteViews(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic")


class NewCreateViews(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewForm
    success_url = reverse_lazy("newspaper:topic")


class NewUpdateViews(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewForm
    success_url = reverse_lazy("newspaper:topic")


class NewDeleteViews(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:topic")
