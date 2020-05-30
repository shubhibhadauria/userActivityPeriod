from django.contrib import admin

from .models import UserActivityPeriod


class UserActivityPeriodAdmin(admin.ModelAdmin):
    list_display = ('real_name','tz','start_time','end_time')


admin.site.register(UserActivityPeriod, UserActivityPeriodAdmin)