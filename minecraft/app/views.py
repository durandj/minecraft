"""
Minecraft app views
"""

from django.views import generic as django_views

class HomeView(django_views.TemplateView):
	"""
	The home view
	"""

	template_name = 'home.html'

