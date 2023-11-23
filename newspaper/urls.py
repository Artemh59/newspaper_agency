from django.urls import path

from newspaper.views import (
    About,
    Index,
    TopicViews,
    NewspaperDetailViews,
)

urlpatterns = [
    path('about_us/', About.as_view(), name='about-us'),
    path('', Index.as_view(), name='index'),
    path('topics/', TopicViews.as_view(), name='topic'),
    path('topics/<int:pk>', NewspaperDetailViews.as_view(), name='topic-detail'),
]

app_name = 'newspaper'
