from .models import Subject, People, Answer, Sex
from django.contrib import admin

admin.site.site_header = 'Museu da Pessoa | Administrative Dashboard'


class SexAdmin(admin.ModelAdmin):
    list_display = ('sex', 'created')
    list_filter = ('created',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'name', 'subject', 'created')
    list_filter = ('created',)


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'created')
    list_filter = ('created',)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'created')
    list_filter = ('created',)


admin.site.register(Sex, SexAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Subject, SubjectAdmin)
