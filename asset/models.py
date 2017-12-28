import datetime
from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django import forms

class Record(models.Model):
    ASSET_TYPE = (
        (0, '笔记本或台式机'),
        (1, '服务器'),
        (2, '其他设备'),
    )
    asset_type = models.IntegerField('资产类型', choices=ASSET_TYPE,default=0)
    asset_number = models.CharField('资产编号',null=True,max_length=200,help_text='一般为设备唯一识别码')
    buy_date = models.DateTimeField('采购时间',null=True,default = timezone.now)
    conf_info = models.TextField('配置信息',max_length=400,null=True,blank=True)
    store_place = models.CharField('存放地点',max_length=400,null=True,blank=True)
    get_time = models.DateTimeField('领用时间',null=True,default = timezone.now)
    user_name = models.CharField('领用人',max_length=50,null=True,blank=True)
    ASSET_STATUS = (
        (True,'完好'),
        (False,'故障')
    )
    asset_status = models.BooleanField('设备状态',choices=ASSET_STATUS,default=True);
    content_text = models.TextField('备注信息',max_length=500,blank=True)
    def get_timed(self):
        return format_html(str(self.get_time))
    get_timed.short_description = '领用时间'

    def buy_dated(self):
        return format_html(str(self.buy_date))
    buy_dated.short_description = '采购时间'



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

