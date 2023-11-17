from django.urls import path
from.import views

urlpatterns = [
    path('viewall/',views.ViewAll,name="viewall"),
    path('add/', views.AddPost, name="add"),

    path('search/', views.searchView, name="search"),
    path('delete/', views.deleteView, name="delete"),
    path('sign/', views.Signup, name="sign"),
]