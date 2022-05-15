from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views
from .views import QuoteDetailView, QuoteCreateView



app_name = 'quote'
urlpatterns = [
    path('', views.QuoteListView.as_view(), name='quotes'),
    path('<int:pk>', QuoteDetailView.as_view(), name='quote'),
    path('<int:pk>/update/', views.QuoteUpdateView.as_view(), name='quote_update'),
    path('<int:pk>/delete/', views.QuoteDeleteView.as_view(), name='quote_delete'),
    path('create', login_required(views.create_quote), name='quote_create')
]
