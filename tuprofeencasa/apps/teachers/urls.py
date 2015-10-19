from django.conf.urls import include, url
from .views import WorkWithUsView


urlpatterns = [
    url(r'^trabaja-con-nosotros/$', WorkWithUsView.as_view(), name='workus'),
]
