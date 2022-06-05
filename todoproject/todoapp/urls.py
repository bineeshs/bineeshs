from . import views

from django.urls import path

urlpatterns = [

    path('',views.add, name="add"),
    path('delete/<int:taskid>/',views.delete,name='DELETE'),
    path('update/<int:id>/',views.update,name='UPDATE'),
    path('cbvhome/',views.Task_Listview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Task_detailview.as_view(),name='CBVDETAILS'),
    path('cbvupdate/<int:pk>/',views.Task_updateview.as_view(),name='CBVUPDATE'),
    path('cbvdelete/<int:pk>/',views.Task_Deleteview.as_view(),name='CBVDELETE'),
]