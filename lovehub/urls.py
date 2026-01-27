from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path("about/", views.about, name="about"),
    path("logout/", views.logout_view, name="logout"),
    path("memories/", views.memories, name="memories"),
    path("love-notes/", views.love_notes, name="love_notes"),
    path("important-dates/", views.important_dates, name="important_dates"),
    path("love-letters/", views.love_letters, name="love_letters"),
    path("check-users/", views.check_users, name="check_users"),  # Keep for now
]