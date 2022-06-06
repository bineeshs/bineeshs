from . import views
from django.urls import path

app_name='movieapp'

urlpatterns = [
    path('',views.index, name="index"),
    path('movie/<int:movie_id>/',views.detail,name="DETAILS"),
    path('add/', views.add_movie, name="add_movie"),
    path('update/<int:id>/',views.update, name='UPDATE'),
    path('delete/<int:id>/',views.delete, name='DELETE')
]