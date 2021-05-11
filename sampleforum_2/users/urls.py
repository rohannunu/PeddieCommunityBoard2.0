from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('editProfile/', views.UserEditView.as_view(), name='editProfile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/changePassword.html')),
    path('password/', views.PasswordsChangeView.as_view(template_name='registration/changePassword.html')),
    path('passwordSuccess/', views.passwordSuccess, name='passwordSuccess'),
    path('<int:pk>/profile/', views.ShowProfilePageView.as_view(), name='showProfilePage'),
    path('<int:pk>/edit_profile_page/', views.EditProfilePageView.as_view(), name='editProfilePage'),
]