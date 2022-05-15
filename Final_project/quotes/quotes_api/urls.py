from django.urls import path, include
from rest_framework import routers
from .views import QuoteListViewSet, RegisterAPI, LoginAPI
from knox import views as knox_views

router = routers.DefaultRouter()
router.register('quotes', QuoteListViewSet)


app_name = 'quotes_api'
urlpatterns = [
    path("", include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout')
]