from django.urls import path

urlpatterns = [
    path('snippet_list/', vies.snippet_list,name="snippet_listsnippet_list"),
    path('api/',include('api.urls')),
]
