# Generated by Django 3.0.3 on 2020-03-03 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('museu', '0003_auto_20200303_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]