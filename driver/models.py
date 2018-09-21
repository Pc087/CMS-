from django.db import models
from django.contrib.auth import settings

# Create your models here.
class Department(models.Model):
    """
    部门列表
    """
    name = models.CharField('部门', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = verbose_name

# 依据用户部门显示可参看及编辑的司机

class DriverQueryset(models.QuerySet):
    def xishu(self):
        """西蜀部门司机"""
        return self.filter(department__name='西蜀')

    def dongwu(self):
        """东吴部门司机"""
        return self.filter(department__name='东吴')

    def beiwei(self):
        """北魏部门司机"""
        return self.filter(department__name='北魏')

class Driver(models.Model):
    """
    司机列表
    """
    CHOICES = (
        ('1', '白班'),
        ('2', '夜班'),
        ('3', '顶班'),
    )
    name = models.CharField('司机姓名', max_length=20)
    work_number = models.CharField('上岗证号', max_length=10, unique=True)
    car_number = models.CharField('车牌号码', max_length=10)
    tel = models.CharField('联系方式', max_length=50, null=True, blank=True)
    scheduling = models.CharField('值班情况', max_length=50, choices=CHOICES, null=True, blank=True)
    place = models.CharField('交班地点', max_length=100, null=True, blank=True)
    department = models.ForeignKey(Department, related_name='drivers', on_delete=models.CASCADE, verbose_name='部门', null=True, blank=True)

    driver = DriverQueryset.as_manager()

    def __str__(self):
        return f'{self.work_number}{self.name}'

    class Meta:
        verbose_name = "司机列表"
        verbose_name_plural = verbose_name

