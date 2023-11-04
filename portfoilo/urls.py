from django.urls import path
from portfoilo import views

app_name = 'portfoilo'

urlpatterns = [
    path('', views.home_page, name="home"),
    path('home/', views.home_page, name="home"),
    path('about/', views.about_me, name="about"),
    path('contact/', views.contact_me, name="contact"),
    path('messages/', views.view_messages, name="view-messages"),
    path('components/', views.components, name="view-components"),
    ]
