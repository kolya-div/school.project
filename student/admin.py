from django.contrib import admin
from .models import StudentModel
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display =     list_display = ('id', 'name', 'surname', 'birthday', 'ade', 'username', 'email')


admin.site.register(StudentModel,StudentAdmin)