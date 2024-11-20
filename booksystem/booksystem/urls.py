from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

# Redirect root URL to books/ app
def home_redirect(request):
    return redirect('accounts/login')

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),  # Include books app URLs
    path('', home_redirect),  # Redirect the root URL to /books/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)