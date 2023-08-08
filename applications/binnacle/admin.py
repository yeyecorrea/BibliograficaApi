from django.contrib import admin
from .models import Binnacle, BinnacleProgres, BinnacleQualification, BinnacleState
# Register your models here.
admin.site.register(Binnacle)
admin.site.register(BinnacleProgres)
admin.site.register(BinnacleQualification)
admin.site.register(BinnacleState)