from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('test_app.urls')),
    path('listings/', include('listings.urls')),
    path('accounts', include('accounts.urls')),
    path('contacts', include('contacts.urls')),
    path('testimo', include('testimo.urls')),
] + static.static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
