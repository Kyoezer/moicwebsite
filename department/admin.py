from django.contrib import admin

from department.models import *


class DoatAdmin(admin.ModelAdmin):
    list_display = ('directorName', 'directorPost', 'directorMail', 'directorPhoneNumber')


admin.site.register(doat, DoatAdmin)


class DittAdmin(admin.ModelAdmin):
    list_display = ('directorName', 'directorPost', 'directorMail', 'directorPhoneNumber')


admin.site.register(ditt, DittAdmin)


class DoimAdmin(admin.ModelAdmin):
    list_display = ('directorName', 'directorPost', 'directorMail', 'directorPhoneNumber')


admin.site.register(doim, DoimAdmin)


class RstaAdmin(admin.ModelAdmin):
    list_display = ('directorName', 'directorPost', 'directorMail', 'directorPhoneNumber')


admin.site.register(rsta, RstaAdmin)
