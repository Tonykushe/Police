# Generated by Django 2.0.1 on 2018-01-25 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimes', '0003_auto_20180125_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='crimesreported',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]