# Generated by Django 2.1 on 2017-12-26 14:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0005_auto_20171226_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
    ]
