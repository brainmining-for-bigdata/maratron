"""ttsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.shortcuts import redirect

# media 파일 연결위해
from django.conf import settings  # settings.py에서 설정한 내용 import
from django.conf.urls.static import static  # urlpatterns 연결위해

urlpatterns = [
    path('', lambda aa : redirect("tts:index")),
    path('admin/', admin.site.urls),
    path('tts/', include('tts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)