# Generated by Django 3.2.14 on 2022-12-01 11:39

import uuid

import django.core.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acls', '0005_auto_20221201_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandGroup',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('org_id',
                 models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('type', models.CharField(choices=[('command', 'Command'), ('regex', 'Regex')], default='command',
                                          max_length=16, verbose_name='Type')),
                ('content', models.TextField(help_text='One line one command', verbose_name='Content')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('ignore_case', models.BooleanField(default=True, verbose_name='Ignore case')),
            ],
            options={
                'verbose_name': 'Command filter rule',
                'unique_together': {('org_id', 'name')},
            },
        ),
        migrations.CreateModel(
            name='CommandFilterACL',
            fields=[
                ('org_id',
                 models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('priority', models.IntegerField(default=50, help_text='1-100, the lower the value will be match first',
                                                 validators=[django.core.validators.MinValueValidator(1),
                                                             django.core.validators.MaxValueValidator(100)],
                                                 verbose_name='Priority')),
                ('action', models.CharField(default='reject', max_length=64, verbose_name='Action')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('comment', models.TextField(blank=True, default='', verbose_name='Comment')),
                ('users', models.JSONField(verbose_name='User')),
                ('accounts', models.JSONField(verbose_name='Account')),
                ('assets', models.JSONField(verbose_name='Asset')),
                ('commands', models.ManyToManyField(to='acls.CommandGroup', verbose_name='Commands')),
                (
                    'reviewers',
                    models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Reviewers')),
            ],
            options={
                'verbose_name': 'Command acl',
                'ordering': ('priority', '-date_updated', 'name'),
                'unique_together': {('name', 'org_id')},
            },
        ),
    ]