# Generated by Django 2.1.5 on 2019-04-13 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0013_question_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='figure',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
