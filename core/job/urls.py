from django.urls import path

from . import views


app_name='job'

urlpatterns = [
    path('listview/',views.listview,name='listview'),
    path('add_to_wishlist/',views.add_product_wish_list,name='add_product_wish_list'),
    path('wishlist/',views.wish_list,name='wish_list'),
    path('det/<id>/',views.detailview,name='detailview'),
    path('search/',views.searchlistview,name='searchlistview')
]
