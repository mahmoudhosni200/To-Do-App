from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from toD import urls 
from User import urls as user_urls # type: ignore



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' , include(urls)),
    path('user/', include(user_urls)),  # Include user URLs
]
