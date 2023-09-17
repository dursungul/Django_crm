from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_req,name='home'),
    path('index',views.index_req,name='index'),
#    path('login/',views.login_user,name='login'),
     path('logout/',views.logout_user,name='logout'),
     path('regiister/',views.register_user,name='register'),
]