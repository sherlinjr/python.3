from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('', views.value,name='value'),
    # path('details',views.details,name="details")
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('newfun/',views.taskview.as_view(),name='newfun'),
    path('newdetail/<int:pk>/',views.taskdetail.as_view(),name='newdetail'),
    path('newupdate/<int:pk>/',views.taskupdate.as_view(),name='newupdate'),
    path('newdelete/<int:pk>/',views.taskdelete.as_view(),name='newdelete'),
]
