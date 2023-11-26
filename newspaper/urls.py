from django.urls import path

from newspaper.views import (
    AboutUsView,
    Index,
    TopicViews,
    TopicDetailViews,
    TopicDeleteViews,
    TopicCreateViews,
    NewCreateViews,
    NewUpdateViews,
    NewDeleteViews,
)

urlpatterns = [
    path('about_us/', AboutUsView.as_view(), name='about-us'),
    path('', Index.as_view(), name='index'),
    path('topics/', TopicViews.as_view(), name='topic'),
    path('topics/create', TopicCreateViews.as_view(), name='topic-create'),
    path('topics/<int:pk>/', TopicDetailViews.as_view(), name='topic-detail'),
    path('topics/delete/<int:pk>/', TopicDeleteViews.as_view(), name='topic-delete'),
    path('news/create', NewCreateViews.as_view(), name='new-create'),
    path('new/update/<int:pk>/', NewUpdateViews.as_view(), name='new-update'),
    path('new/delete/<int:pk>/', NewDeleteViews.as_view(), name='new-delete'),
]

app_name = 'newspaper'
