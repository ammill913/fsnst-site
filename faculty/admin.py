from django.contrib import admin

from .models import Department, ExchangeProgram, HomeContent, Program, Teacher

admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Teacher)
admin.site.register(HomeContent)
admin.site.register(ExchangeProgram)

# Register your models here.
