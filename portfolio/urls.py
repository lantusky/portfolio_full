from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('projects/re/', include('pages.urls')),
    path('projects/re/listings/', include('listings.urls')),
    path('projects/re/accounts/', include('accounts.urls')),
    path('projects/re/contacts/', include('contacts.urls')),
    path('projects/re/admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
