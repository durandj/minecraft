"""
Minecraft app views
"""

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

