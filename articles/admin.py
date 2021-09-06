from django.contrib import admin


from .models import Articles,GeneralSetting,Menu

admin.site.register(Articles)
admin.site.register(GeneralSetting)
admin.site.register(Menu)
# Register your models here.
