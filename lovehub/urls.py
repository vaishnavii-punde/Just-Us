from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),  # login page
    path('', views.home, name='home'),              # home page after login
    path("about/", views.about, name="about"),   # ✅ THIS LINE
    path("logout/", views.logout_view, name="logout"),
    
]
