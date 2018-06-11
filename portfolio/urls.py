from django.urls import path

from . import views

urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<int:pk>/', views.portfolio_detail, name='portfolio-detail'),
]