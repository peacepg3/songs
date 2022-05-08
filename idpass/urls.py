# from .import views
# from django.urls import path
#
# urlpatterns = [
#     path('',views.idapp,name='idapp'),
#     path('pgattribute/<int:ids>',views.details,name='details'),
#     path('update',views.update,name='add-update'),
#     path('<int:year>/<str:month>/',views.calender,name='calender'),
#     path('updateatt/<int:ide>',views.updateatt,name='updateatt'),
#     path('delte/<int:ide>', views.delte, name='delte'),
# ]
from django.urls import path
from . import views

urlpatterns =[
    path('search/', views.search_song, name='search-song'),
    path('',views.songview,name='songview'),
    path('<slug:slg_variable>/',views.songview,name='sng_vw'),
    path('<slug:c_slug>/<slug:prod_variable>/',views.prod_detail, name='det'),
]