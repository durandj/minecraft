"""
Minecraft app views
"""

from django import shortcuts as django_shortcuts
from django.contrib import auth as django_auth
from django.core import urlresolvers as django_urlresolvers
from django.views import generic as django_views

from minecraft.app import models as minecraft_models

class HomeView(django_views.TemplateView):
	"""
	The home view
	"""

	template_name = 'home.html'

	def get_context_data(self, **kargs):
		"""
		Add the update info to the context.
		"""

		context = {
			'mod_updates': minecraft_models.Mod.objects.order_by('last_edited_by')[:5],
			'modpack_updates': minecraft_models.Modpack.objects.order_by('last_edited_by')[:5],
		}

		return super(HomeView, self).get_context_data(**context)

class ModsView(django_views.ListView):
	"""
	The mods view
	"""

	context_object_name = 'mods'
	model               = minecraft_models.Mod
	template_name       = 'mods.html'

class ModView(django_views.DetailView):
	"""
	The mod detail view
	"""

	context_object_name = 'mod'
	model               = minecraft_models.Mod
	template_name       = 'mod.html'

class ModpacksView(django_views.ListView):
	"""
	The modpacks view
	"""

	context_object_name = 'modpacks'
	model               = minecraft_models.Modpack
	template_name       = 'modpacks.html'

class ModpackView(django_views.DetailView):
	"""
	The modpack detail view
	"""

	context_object_name = 'modpack'
	model               = minecraft_models.Modpack
	template_name       = 'modpack.html'

class LoginView(django_views.TemplateView):
	"""
	The login view
	"""

	template_name = 'login.html'

	def post(self, request, *args, **kwargs):
		"""
		Handle login attempt
		"""

		username = request.POST['username']
		password = request.POST['password']

		next = request.POST['next'] if 'next' in request.POST else django_urlresolvers.reverse('home')

		user = django_auth.authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				django_auth.login(request, user)
				return django_shortcuts.redirect(next)
			else:
				return None # TODO: login error
		else:
			return None # TODO: login error

class LogoutView(django_views.View):
	"""
	The logout view
	"""

	def post(self, request, *args, **kwargs):
		"""
		Handle logout attempt
		"""

		home_url = django_urlresolvers.reverse('home')
		django_auth.logout(request)
		return django_shortcuts.redirect(home_url)

