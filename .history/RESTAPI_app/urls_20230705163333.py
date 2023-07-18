from django.urls import path
from views import snippet_list
urlpatterns = [
    path('snippet_list/', views.snippet_list,name="snippet_list"),
    
]
