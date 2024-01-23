from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('pass_change/' ,views.pass_change, name='pass_change' ),
    path('pass_reset/' ,views.pass_reset, name='pass_reset' ),
]
