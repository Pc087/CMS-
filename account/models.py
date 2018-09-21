from django.db import models
from django.contrib.auth import settings
from driver.models import Department

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='用户名')
    department = models.ForeignKey(Department, related_name='profile', on_delete=models.CASCADE, verbose_name='部门',
                                   null=True, blank=True)
    cpt_add = models.BooleanField('投诉新增功能', default=False)
    cpt_delete = models.BooleanField('投诉删除功能', default=False)
    cpt_edit = models.BooleanField('投诉编辑功能', default=False)
    driver_add = models.BooleanField('司机新增功能', default=False)
    driver_delete = models.BooleanField('司机删除功能', default=False)
    driver_edit = models.BooleanField('司机编辑功能', default=False)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = '用户权限'
        verbose_name_plural = verbose_name
