from django.contrib.auth.admin import Group
from django.contrib import admin
from .models import Messages

admin.site.site_header = 'Museu da Pessoa'


class MessageAdmin(admin.ModelAdmin):
    list_display = ('content', 'datetime')
    list_filter = ('title', )


admin.site.register(Messages, MessageAdmin)
admin.site.unregister(Group)
