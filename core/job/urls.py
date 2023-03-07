from django.urls import path

from . import views


urlpatterns = [
    path('listview/',views.listview,name='listview')
]
