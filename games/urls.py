from django.urls import include, re_path
from games import views 
 
urlpatterns = [ 
    re_path(r'^games/$', views.game_collection), 
    re_path(r'^games/(?P<id>[0-9]+)/$', views.game_detail), 
] 