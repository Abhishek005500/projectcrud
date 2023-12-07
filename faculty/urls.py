from django.urls import path
from faculty import views
urlpatterns = [
    path('register/', views.register,name="register"),
    path('login/', views.login_view,name="login"),
    path('logout/', views.logout_view,name="logout"),
]
