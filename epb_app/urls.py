# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from epb_app import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', views.login, name='login'),
    path('apply/', views.apply_now, name='apply_now'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('success/', views.success, name='success')
]
   
    

