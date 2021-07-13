"""projeto_escala_hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('painel/', admin.site.urls),
    path('', include('escala.urls', namespace='escala')),
    path('medicos/', include('medico.urls', namespace='medicos')),
    path('postos/', include('posto.urls', namespace='posto')),
    path('folga/', include('folga.urls', namespace='folga')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Customização do admin
admin.AdminSite.site_header = 'Escala de Atendimento'
admin.AdminSite.site_title = 'Controle Escala'
admin.AdminSite.index_title = 'Escala Administração'
