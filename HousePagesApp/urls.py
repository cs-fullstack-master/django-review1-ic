from django.urls import path
from . import views



urlpatterns = [
    path("", views.tonOPages, name="index"),
    # path("pages/", views.tonOPages, name="ton"),
    path("add5/", views.add5, name="add5"),
    path("sub10/", views.sub10, name="sub10"),
    path("mult2/", views.mult2, name="mult2"),
    path("div10/", views.div10, name="div10"),
    path("details/<int:houseID>", views.details, name="details")
]