"""eventex URL Configuration

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

#django 2.1
#from django.contrib import admin
#from django.urls import path

#import eventex.core.views
#from eventex.subscriptions.views import subscribe

#Usando Django 1.9
from django.conf.urls import url
from django.contrib import admin

from eventex.core.views import home
from eventex.subscriptions.views import subscribe

#django 2.1
#urlpatterns = [
#    path('', eventex.core.views.home),
#    path('inscricao/', subscribe),
#    path('admin/', admin.site.urls),
#]
urlpatterns = [
    url(r'^$', home),
    url(r'^inscricao/$', subscribe),
    url(r'^admin/', admin.site.urls),
]
"""
"""eventex URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
import eventex.core.views
from eventex.subscriptions.views import subscribe

urlpatterns = [
    path('', eventex.core.views.home),
    path('inscricao/', subscribe),
    path('admin/', admin.site.urls),
]
