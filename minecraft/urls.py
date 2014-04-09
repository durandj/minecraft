"""
Minecraft site URLs
"""

# pylint: disable=E1120

from django.conf.urls import patterns, url

from minecraft.app import views as minecraft_views

urlpatterns = patterns('',
	url(r'^$',						minecraft_views.HomeView.as_view(),		name = 'home'),
	url(r'^mods$',					minecraft_views.ModsView.as_view(),		name = 'mods'),
	url(r'^mods/(?P<pk>\d+)$',		minecraft_views.ModView.as_view(),		name = 'mod'),
	url(r'^modpacks$',				minecraft_views.ModpacksView.as_view(),	name = 'modpacks'),
	url(r'^modpacks/(?P<pk>\d+)$',	minecraft_views.ModpackView.as_view(),	name = 'modpack'),
	url(r'^login$',					minecraft_views.LoginView.as_view(),	name = 'login'),
	url(r'^logout$',				minecraft_views.LogoutView.as_view(),	name = 'logout'),
)

