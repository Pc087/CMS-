# Generated by Django 2.1.1 on 2018-09-19 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0007_auto_20180918_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complaint_number',
            field=models.CharField(default='20180919114738210', max_length=20, unique=True, verbose_name='投诉编号'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='附件'),
        ),
    ]
