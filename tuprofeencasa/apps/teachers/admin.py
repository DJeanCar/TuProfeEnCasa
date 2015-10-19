from django.contrib import admin
from .models import Occupation, Teacher

@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
	pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	pass