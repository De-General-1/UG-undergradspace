# Generated by Django 4.0.3 on 2022-04-25 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_report_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='isUpdated',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
