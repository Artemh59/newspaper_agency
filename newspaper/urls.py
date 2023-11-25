from django.urls import path

from newspaper.views import (
    AboutUsView,
    Index,
    TopicViews,
    TopicDetailViews,
)

urlpatterns = [
    path('about_us/', AboutUsView.as_view(), name='about-us'),
    path('', Index.as_view(), name='index'),
    path('topics/', TopicViews.as_view(), name='topic'),
    path('topics/<int:pk>/', TopicDetailViews.as_view(), name='topic-detail'),
]

app_name = 'newspaper'
