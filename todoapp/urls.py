from django.urls import path
from . import views
urlpatterns = [
    path('',views.todo,name='todo'),
    path('dlt/<int:dltid>',views.delt,name='delt'),
    path('upd/<int:updateid>',views.update,name='update'),
    path('generic/',views.listview.as_view(),name='generic'),
    path('details/<int:pk>/',views.detailview.as_view(),name='details'),
    path('update/<int:pk>/',views.updateview.as_view(),name='update'),
    path('delete/<int:pk>/', views.updateview.as_view(), name='delete'),

]