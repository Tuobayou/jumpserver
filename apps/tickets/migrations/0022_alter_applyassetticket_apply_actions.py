# Generated by Django 3.2.14 on 2022-11-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0021_auto_20220921_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyassetticket',
            name='apply_actions',
            field=models.IntegerField(default=1, verbose_name='Actions'),
        ),
    ]
