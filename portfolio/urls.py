from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('projects/re/', include('pages.urls')),
    path('projects/re/listings/', include('listings.urls')),
    path('projects/re/accounts/', include('accounts.urls')),
    path('projects/re/contacts/', include('contacts.urls')),
    path('admin', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
