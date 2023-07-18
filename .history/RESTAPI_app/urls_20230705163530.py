from django.urls import path
from RES import views
urlpatterns = [
    path('snippet_list/', views.snippet_list,name="snippet_list"),
    
]
