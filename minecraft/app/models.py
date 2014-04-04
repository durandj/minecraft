"""
Minecraft site models
"""

from django.contrib.auth import models as auth_models
from django.db import models as django_models

class Mod(django_models.Model):
	"""
	A Minecraft modification.
	"""

	name    = django_models.CharField(max_length = 256, unique = True)
	url     = django_models.URLField()
	version = django_models.CharField(max_length = 64)

	created_by     = django_models.ForeignKey(auth_models.User, related_name = 'mod_created_by')
	created_on     = django_models.DateTimeField(auto_now_add = True)
	last_edited_by = django_models.ForeignKey(auth_models.User, null = True)
	last_edited_on = django_models.DateTimeField(auto_now = True, null = True)

class Modpack(django_models.Model):
	"""
	A modpack is a collection of mods.
	"""

	name = django_models.CharField(max_length = 256, unique = True)
	url  = django_models.URLField()

	created_by     = django_models.ForeignKey(auth_models.User, related_name = 'modpack_created_by')
	created_on     = django_models.DateTimeField(auto_now_add = True)
	last_edited_by = django_models.ForeignKey(auth_models.User, null = True)
	last_edited_on = django_models.DateTimeField(auto_now = True, null = True)

class ModpackMod(django_models.Model):
	"""
	A mod in a modpack
	"""

	mod     = django_models.ForeignKey(Mod)
	modpack = django_models.ForeignKey(Modpack)

	created_by     = django_models.ForeignKey(auth_models.User, related_name = 'modpack_mod_created_by')
	created_on     = django_models.DateTimeField(auto_now_add = True)
	last_edited_by = django_models.ForeignKey(auth_models.User, null = True)
	last_edited_on = django_models.DateTimeField(auto_now = True, null = True)

class Link(django_models.Model):
	"""
	A link that should be displayed in the nav bar
	"""

	name = django_models.CharField(max_length = 256, unique = True)
	url  = django_models.URLField()

