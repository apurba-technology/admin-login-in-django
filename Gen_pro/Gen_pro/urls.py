"""Gen_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from Next_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin', views.admin, name='admin'),
    path('', views.index, name='home'),
    path('banner_upload', views.banner_upload, name='banner_upload'),
    path('display', views.display_images, name= 'display_images' ),
    path('delete/<int:id>', views.delete),
    path('notice', views.notice_upload),
    path('display_notice',views.disNo, name='display_notice'),
    path('delet/<int:id>', views.delet),
    path('programme', views.programme_upload),
    path('regestion',views.admin_regestion),
    path('log',views.log_in, name='log' ),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
