from django.contrib import admin

from .models import Person, Skill, Professional, Formation


class ProfessionalInline(admin.TabularInline):
    model = Professional
    extra = 3


class FormationInline(admin.TabularInline):
    model = Formation
    extra = 3


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 3


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'birth_date')
    inlines = [
        ProfessionalInline,
        FormationInline,
        SkillInline
    ]


# Register
admin.site.register(Person, PersonAdmin)
