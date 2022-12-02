from django.contrib import admin
from django.urls import include,path
from . import views
urlpatterns = [
    path('',views.index,name='vente_index'),
    path('<int:id>',views.show,name='show_produit')
]
