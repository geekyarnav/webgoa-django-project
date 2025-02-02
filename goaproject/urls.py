"""goaproject URL Configuration

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
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from packagesapp.views import homeview,aboutview,contactview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^$', homeview,name=''),
    # path('contact/',contactview,name="contact"),
    # path('about/',aboutview,name="about"),
    url(r'^blogs/', include('blogsapp.urls')),
    url(r'^events/', include('eventsapp.urls')),
    url(r'^', include('packagesapp.urls'))
    ]
    # url(r'^packages/', include('packagesapp.urls'))
    # path('', views.home, name='home')
    # url(r'^about-us/', include('urls')),
    # url(r'^contact-us/$', include('urls')), 

urlpatterns=urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)