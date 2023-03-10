from django.contrib.auth.views import LogoutView
from django.urls import path
from users.views import login_view, register,update_user,update_user_profile,list_profile,ProfileDeleteView

urlpatterns = [
    path('login/', login_view, name = 'login'),
    path('logout/',LogoutView.as_view(template_name = 'users/logout.html')),
    path('signup/',register),
    path('update_user/',update_user),
    path('update/profile/', update_user_profile),
    path('list_profile/', list_profile),
    path('delete_profile/<int:pk>/', ProfileDeleteView.as_view()),
]