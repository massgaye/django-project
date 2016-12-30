from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Personne)
admin.site.register(Situation)
admin.site.register(Centre)
admin.site.register(TypeSituation)
admin.site.register(Service)
admin.site.register(Appelant)
admin.site.register(Appel)
admin.site.register(Hebergement)
admin.site.register(Beneficier)
admin.site.register(etre)


