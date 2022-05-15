from django.urls import path, include
from . import views

app_name = 'my_auth'
urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path("users/", include("django.contrib.auth.urls")),
    # path("send_email/", views.send_email),
]