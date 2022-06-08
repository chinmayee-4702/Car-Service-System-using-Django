import imp
from operator import contains
from django.contrib import admin
from.models import Appoint, Contact
# Register your models here.

admin.site.register(Appoint),
admin.site.register(Contact),
# admin.site.register(Feedback)