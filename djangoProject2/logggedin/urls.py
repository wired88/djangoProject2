from django.urls import path
from . import views

# in dieses File kommen alle urls welche die App bereitstellt
app_name = 'logggedin'
urlpatterns = [
    path('', views.index, name='index'),
]