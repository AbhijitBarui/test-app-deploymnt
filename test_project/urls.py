from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('test_app.urls')),
    path('listings', include('listings.urls')),
]
