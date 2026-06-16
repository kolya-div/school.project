from django.contrib import admin
from .models import TecherModel
# Register your models here.

class TecherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'birthday', 'ade', 'username', 'email')

admin.site.register(TecherModel,TecherAdmin)