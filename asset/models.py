import datetime
from django.db import models
from django.utils import timezone

class Record(models.Model):
    ASSET_TYPE = (
        (0, '笔记本或台式机'),
        (1, '服务器'),
        (2, '其他设备'),
    )
    asset_type = models.IntegerField('资产类型', choices=ASSET_TYPE,default=0)
    asset_number = models.CharField('资产编号',null=True,max_length=200,help_text='一般为设备唯一识别码')
    buy_date = models.DateTimeField('采购时间',null=True)
    conf_info = models.CharField('配置信息',max_length=400,null=True,blank=True)
    store_place = models.CharField('存放地点',max_length=400,null=True,blank=True)
    get_time = models.DateTimeField('领用时间',null=True)
    user_name = models.CharField('领用人',max_length=50,null=True,blank=True)
    send_user = models.CharField('发送人',max_length=50,null=True,blank=True)
    ASSET_STATUS = (
        (True,'完好'),
        (False,'故障')
    )
    #asset_status = models.BooleanField('设备状态',choices=ASSET_STATUS,default=True);
    # asset_type = models.IntegerField(default=1) #1,笔记本或普通台式机；2，服务器；3，其他
    send_date = models.DateTimeField('发放时间')
    # content_text = models.CharField(max_length=500)
    content_text = models.TextField(max_length=500,blank=True)
    #
    # SHIRT_SIZES = (
    #     ('S', 'Small'),
    #     ('M', 'Medium2'),
    #     ('L', 'Large'),
    # )
    # shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES,default='M',help_text="这是帮助内容")
    def __str__(self):              # __unicode__ on Python 2
        return str(self.asset_type)

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