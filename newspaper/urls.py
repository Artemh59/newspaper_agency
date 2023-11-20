from django.urls import path

from newspaper.views import About, Index

urlpatterns = [
    path('about_us/', About.as_view(), name='about-us'),
    path('', Index.as_view(), name='index'),
]

app_name = 'newspaper'
