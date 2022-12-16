from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("richarlison", views.richarlison, name="richarlison"),
	path("camisadez", views.camisadez, name="camisadez"),
	path("<str:name>", views.greet, name="greet")
]
