from django.urls import path

from newspaper.views import About

urlpatterns = [
    path('about_us/', About.as_view(), name='about-us'),
]

app_name = 'newspaper'
