from django.urls import path
from . import views

urlpatterns = [
    path('TazkeraForm/', views.TazkeraForm, name='TazkeraForm'),
    
    path("add/", views.add, name="add"),
    path("admin/TazkeraForm/tazkera/add/", views.add, name="add"),
    path("list/", views.list_tazkera, name="list_tazkera"),

    path(
        "print/<int:pk>/",
        views.print_tazkera,
        name="print_tazkera",
    ),

]