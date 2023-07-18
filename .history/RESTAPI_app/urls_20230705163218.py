

from django.urls import path,inclue

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
]
