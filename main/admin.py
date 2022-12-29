from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Pacient)
admin.site.register(AnalysisRequest)
admin.site.register(Results)

# Register your models here.
