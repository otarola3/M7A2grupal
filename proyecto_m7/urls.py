"""
URL configuration for proyecto_m7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core_m7.views import index_welcome, BienvenidaView, register, listar_productos
from django.contrib.auth import views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_welcome, name="index"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('bienvenida_login/', BienvenidaView.as_view(), name='bienvenida'),
    path('registro/', register, name='registro'),
    path('productos/', listar_productos, name='listar_productos')
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)