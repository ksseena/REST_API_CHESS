from django.urls import path
from . import views

urlpatterns = [
    path('<slug>/', views.get_valid_moves),
]
