from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login_view,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout_view,name='logout'),
    path('chatbot',views.chatbot,name='chatbot'),


]