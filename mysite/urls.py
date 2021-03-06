"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin

from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls', namespace="polls")),
    # path('asset/', include('asset.urls', namespace="asset")),
    #path('polls/',  include('polls.urls')), #匹配并截取polls,然后将剩余的参数传递
    #url(r'^polls/', include('polls.urls')),
    #url(r'^admin/', include(admin.site.urls)),
]