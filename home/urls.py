from urllib import request

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import HomeView, DescriptionView, RegisterView, UserLoginView, ProfileView, SettingsView, \
    UsersRecipesCreateView, UsersRecipesView, RecipeDetailView

# in dieses File kommen alle urls welche die App bereitstellt
app_name = 'home'
urlpatterns = [
    #path('', views.index, name='index'),
    path('', HomeView.as_view(), name='index'),

    path('register/', RegisterView.as_view(), name='register'),

    path('login/', UserLoginView.as_view(), name='login'),
    path('description/', DescriptionView.as_view(), name='description'),
    path('logout/', views.logout_view, name='logout'),
    path('user-recipe/<int:pk>/', RecipeDetailView.as_view(), name='user-recipe'),

    # <pk> is identification for id field,
    # slug can also be used
    # <int:product_id>/ hier wird das Parameter in das base.html file übergeben, damit django weiß, welches Produkt
    # gelöscht werden soll
    #path('delete/<int:pk>/', DeleteObjectView.as_view(), name='delete'),
    path('delete/<int:pk>/', views.delete_view, name='delete'),


    path('my-recipes/', UsersRecipesView.as_view(), name='my-recipes'),
    path('create/', UsersRecipesCreateView.as_view(), name='create'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('password/', auth_views.PasswordChangeView.as_view(), name='password'),
]

