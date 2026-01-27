from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path("about/", views.about, name="about"),
    path("logout/", views.logout_view, name="logout"),
    path("memories/", views.memories, name="memories"),
    path("check-users/", views.check_users, name="check_users"),
]