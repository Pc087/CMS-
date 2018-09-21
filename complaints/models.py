from django.db import models
from django.contrib.auth import settings
import datetime
import time
import random

# Create your models here.

class ComplaintQuerySet(models.QuerySet):
    def this_year(self):
        return self.filter(record_date__year=time.localtime().tm_year)

    def nofinished(self):
        return self.filter(is_finished=False)


class Complaint(models.Model):
    """
    投诉列表
    """
    CATEGORY_CHOICES = (
        ('1', '投诉'),
        ('2', '失物查找'),
        ('3', '其他'),
    )
    title = models.CharField('标题', max_length=50)
    complaint_number = models.CharField('投诉编号', max_length=20, default=str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))+''.join(random.sample('0123456789', 3)), unique=True)
    category = models.CharField('类型', max_length=50, choices=CATEGORY_CHOICES, default='1')
    record_date = models.DateTimeField('登记日期')
    happen_date = models.DateTimeField('事发日期')
    complainant = models.CharField('投诉人', max_length=20)
    tel = models.CharField('投诉人联系方式', max_length=50, null=True, blank=True)
    content = models.TextField('投诉内容', null=True, blank=True)
    feedback_content = models.TextField('处理结果', null=True, blank=True)
    is_finished = models.BooleanField('处理进度', default=False)
    driver_name = models.CharField('司机姓名', max_length=50, blank=True, null=True)
    driver_work_number = models.CharField('服务监督号', max_length=50, blank=True, null=True)
    driver_tel = models.CharField('联系方式', max_length=50, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户名', related_name='complaint_user', null=True, blank=True)
    image = models.ImageField('附件', null=True, blank=True)

    objects = ComplaintQuerySet.as_manager()

    class Meta:
        verbose_name = "投诉列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.title}'