"""inhousemenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import home
from search_recipes.views import search_recipes_form, search_recipes, get_full_recipe
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', home),
    url(r'^search_recipes_form/$', search_recipes_form),
    url(r'^search_recipes/$', search_recipes),
    #url(r'^get_full_recipe/(\d{1,2})/$', get_full_recipe),
    #url(r'^get_full_recipe/$', get_full_recipe),
    url(r'^get_full_recipe/([A-Za-z_]+)/$', get_full_recipe),
]

urlpatterns += staticfiles_urlpatterns()

#if settings.DEBUG :
 #   urlpatterns += patterns('django.contrib.staticfiles.views',
  #      url(r'^static/(?P<path>.*)$', 'serve'),
   # )

