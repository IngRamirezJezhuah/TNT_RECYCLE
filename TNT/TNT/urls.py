"""
URL configuration for TNT project.

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
from django.urls import include, path

urlpatterns = [
    #Incluimos Las Ureles de las App creadas aqui mero
    path('USERS/', include("USERS.urls")),
    path('TRANSACCIONES/', include("TRANSACCIONES.urls")),
    path('FINANZAS/', include("FINANZAS.urls")),
    path('CONTROL/', include("CONTROL.urls")),
    path('AJUSTES/', include("AJUSTES.urls")),
    path('CORTES/', include("CORTES.urls")),
    path('admin/', admin.site.urls),
    
]
