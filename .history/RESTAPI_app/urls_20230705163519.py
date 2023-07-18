from django.urls import path
from . import views
urlpatterns = [
    path('snippet_list/', views.snippet_list,name="snippet_list"),
    
]
