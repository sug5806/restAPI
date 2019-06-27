from django.contrib import admin
from .models import *

# Register your models here.

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'cls_t', 'attendance', 'date']
#
#     def get_products(self, obj):
#         return "\n".join([p.test for p in obj.Student.all()])
#
# admin.site.register(Student, StudentAdmin)
#
# admin.site.register(cls)
#
#
# class TestAdmin(admin.ModelAdmin):
#     list_display = ['test_name', 'day']
#
# admin.site.register(Test, TestAdmin)
#
#
#
# admin.site.register(Date)

admin.site.register(student)

admin.site.register(image)

admin.site.register(name)

admin.site.register(cls_type)

from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    UserAdmin.fieldsets[1][1]['fields'] += ('cls', )

    UserAdmin.add_fieldsets += (
        (('Additional Info'), {'fields': ('profile', 'message')})
    )


admin.site.register(manager, CustomUserAdmin)

