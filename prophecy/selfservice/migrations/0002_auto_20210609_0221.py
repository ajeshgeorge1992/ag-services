# Generated by Django 3.2.4 on 2021-06-09 02:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('selfservice', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='winner',
            old_name='draw_tiem',
            new_name='day',
        ),
        migrations.AddField(
            model_name='winner',
            name='draw_time',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
