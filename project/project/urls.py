"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',base,name='base'),
    path('', home, name='home'),
    path('add_card/', add_card, name='add_card'),
    path('add_item/', add_item, name='add_item'),
    path('show_item/', show_item, name='show_item'),
    path('search/', search, name='search'),
    path('low_to_high',low_to_high, name='low_to_high'),
    path('high_to_low',high_to_low, name='high_to_low'),
    path('arrange_by_name',arrange_by_name, name='arrange_by_name'),
    path('price_between',price_between, name='price_between'),
    path('price_above',price_above, name='price_above'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)