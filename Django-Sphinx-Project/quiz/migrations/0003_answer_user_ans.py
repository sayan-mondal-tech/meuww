# Generated by Django 2.1.5 on 2019-03-21 10:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20190321_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='user_ans',
            field=models.CharField(default=django.utils.timezone.now, max_length=2000, verbose_name='userbyans'),
            preserve_default=False,
        ),
    ]
