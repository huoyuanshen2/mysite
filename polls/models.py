import datetime
from django.db import models
from django.utils import timezone

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
    class Meta:
        permissions = (
            ("scan_question", "自定义查看权限"),
        )


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #question = models.IntegerField(default=0)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #on_delete = models.CASCADE(question)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text