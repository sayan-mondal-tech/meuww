# Generated by Django 2.1.5 on 2019-04-13 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_remove_question_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_link',
            field=models.CharField(default=0, max_length=1800, verbose_name='questionlink'),
            preserve_default=False,
        ),
    ]
