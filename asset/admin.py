from django.contrib import admin
from .models import  Record,Question
# Register your models here.

#admin.site.register(Question)

class RecordAdmin(admin.ModelAdmin):
    # date_hierarchy = 'buy_date'
    # actions_on_top = 'True'
    list_display = ['asset_type','buy_dated','conf_info','asset_status','user_name','get_timed']

    # fieldsets = [  (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
admin.site.register(Record,RecordAdmin)
