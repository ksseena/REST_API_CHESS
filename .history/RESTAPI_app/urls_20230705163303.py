from django.urls import path

urlpatterns = [
    path('snippet_list/', vies.snippet_list),
    path('api/',include('api.urls')),
]
