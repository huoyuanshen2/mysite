# Generated by Django 2.1 on 2017-12-26 14:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_auto_20171226_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='age',
            new_name='asset_type',
        ),
        migrations.AddField(
            model_name='record',
            name='send_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='发放时间'),
            preserve_default=False,
        ),
    ]
