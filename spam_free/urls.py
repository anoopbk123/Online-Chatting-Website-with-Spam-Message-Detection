"""spam_message URL Configuration

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
from django.urls import path, re_path
from django.urls import  re_path, include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('chat/', include('chat.urls')),
     re_path('comment/', include('comment.urls')),
     re_path('friends/', include('friends.urls')),
     re_path('like_photo/', include('like_photo.urls')),
     re_path('login/', include('login.urls')),
     re_path('reported_comments/', include('reported_comments.urls')),
     re_path('share/', include('share.urls')),
     re_path('user_reg/', include('user_reg.urls')),
     re_path('temp/', include('temp.urls')),
     re_path('$', views.login),
]
