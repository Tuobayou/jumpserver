# Generated by Django 3.2.16 on 2023-02-16 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_gatheredaccount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'permissions': [('view_accountsecret', 'Can view asset account secret'), ('view_historyaccount', 'Can view asset history account'), ('view_historyaccountsecret', 'Can view asset history account secret')], 'verbose_name': 'Account'},
        ),
    ]
