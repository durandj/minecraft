"""
Minecraft site URLs
"""

# pylint: disable=E1120

from django.conf.urls import patterns, url

from minecraft.app import views as minecraft_views

urlpatterns = patterns('',
	url(r'^$',				minecraft_views.HomeView.as_view(),	name = 'home'),
	url(r'^mods(/\d+)?$',	minecraft_views.ModsView.as_view(),	name = 'mods'),
)

