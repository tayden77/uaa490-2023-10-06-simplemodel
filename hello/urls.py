from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("marc/", views.marc, name="marc"),
    path("uaa490/", views.uaa490, name="xyz"),
    path("<str:name>/", views.greet, name="greet"),

]