
from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("myapp.urls")),
    path('api/',include("myapp.api.urls")),
    path('',include("healthapp.urls")),
    

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        
        
urlpatterns += staticfiles_urlpatterns()
        
        
        