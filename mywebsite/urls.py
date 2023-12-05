
from django.contrib import admin
from django.urls import path
from myapp  import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),

    path('update/<int:id>', views.update,name="update"),
    path('doupdate/<int:id>', views.doupdate,name="doupdate"),
    
    path('delete/<int:id>', views.delete,name="delete"),
    
    
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        
        
urlpatterns += staticfiles_urlpatterns()
        
        
        