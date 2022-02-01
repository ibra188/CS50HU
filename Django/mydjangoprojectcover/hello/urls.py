from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sonko", views.sonko, name="sonko"),
    path("ibra", views.ibra, name="ibra"),
    path("<str:name>", views.greet, name="greet")
]