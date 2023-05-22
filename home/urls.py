from django.urls import path
from . import views

# in dieses File kommen alle urls welche die App bereitstellt
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('description/', views.description, name='description'),
    path('', views.logout_view, name='logout'),
]
