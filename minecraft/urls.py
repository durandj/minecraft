"""
Minecraft site URLs
"""

# pylint: disable=E1120

from django.conf.urls import patterns, url

from minecraft.app import views as minecraft_views

urlpatterns = patterns('',
	url(r'^$',					minecraft_views.HomeView.as_view(),		name = 'home'),
	url(r'^mods(/\d+)?$',		minecraft_views.ModsView.as_view(),		name = 'mods'),
	url(r'^modpacks(/\d+)?$',	minecraft_views.ModpacksView.as_view(),	name = 'modpacks'),
	url(r'^login$',				minecraft_views.LoginView.as_view(),	name = 'login'),
	url(r'^logout$',			minecraft_views.LogoutView.as_view(),	name = 'logout'),
)

