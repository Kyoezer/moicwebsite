from django.contrib import admin
from organogram.models import top_title, human_resource, organogram, information_download, ministry_strength

# Register your models here.
# admin.site.register(top_title)
# admin.site.register(human_resource)
# admin.site.register(organogram)
# admin.site.register(information_download)


class StrengthAdmin(admin.ModelAdmin):
    list_display = ('year', 'total', 'executives', 'pro_and_mgmt', 'support', 'operational')


admin.site.register(ministry_strength, StrengthAdmin)
