from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    import debug_toolbar
    from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('product/', include('crud.urls')),
    path('register/', include('user_registration.urls')),
    path('log-in/', include('user_login.urls')),
    path('log-out/', include('user_logout.urls')),
    path('vendor-profile/', include('vendor_user_profile.urls', namespace='vendor_user_profile')),
    path('order/', include('order_product.urls')),
    path('', include('messaging.urls')),
    path('__debug__/', include(debug_toolbar.urls)),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
