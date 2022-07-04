from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    #path("", views.IndexView.as_view(), name="index"),
    path("", views.Index, name="index"),
    path("createproduct/", views.createproduct, name="createproduct"),
    #path("", views.DetailView.as_view(), name="detail"),
    #ex: /polls/5/results
    
]