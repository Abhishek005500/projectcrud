
from django.contrib import admin
from django.urls import path,include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework_simplejwt import views as jwt_views 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include("myapp.urls")),
    path('student/api/',include("myapp.api.urls")),
    path('fac/',include("faculty.urls")),
    path('fac/api/',include("faculty.api.urls")),
    
    
    
    
    path('api/token/', 
         jwt_views.TokenObtainPairView.as_view(), 
         name ='token_obtain_pair'), 
    path('api/token/refresh/', 
         jwt_views.TokenRefreshView.as_view(), 
         name ='token_refresh'), 
    path('', include('myapp.urls')), 
    

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        
        
urlpatterns += staticfiles_urlpatterns()
        
        
        