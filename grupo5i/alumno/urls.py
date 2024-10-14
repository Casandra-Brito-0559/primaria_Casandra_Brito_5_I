from django.urls import path
from alumno import views
urlpatterns = [
    path('',views.index_vistas,name="index_vistas"),
]