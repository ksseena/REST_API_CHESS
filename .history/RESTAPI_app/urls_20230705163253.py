from django.urls import path

urlpatterns = [
    path('snippet_list/', admin.site.urls),
    path('api/',include('api.urls')),
]
