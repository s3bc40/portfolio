from django.contrib import admin

from .models import Person, Skill


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'birth_date')


# Register
admin.site.register(Person, PersonAdmin)
admin.site.register(Skill)
