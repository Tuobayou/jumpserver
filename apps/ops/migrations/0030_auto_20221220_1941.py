# Generated by Django 3.2.14 on 2022-12-20 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ops', '0029_auto_20221215_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobAuditLog',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('ops.jobexecution',),
        ),
        migrations.AddField(
            model_name='job',
            name='version',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jobexecution',
            name='job_version',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='HistoricalJob',
            fields=[
                ('created_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, max_length=32, null=True, verbose_name='Updated by')),
                ('date_created', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Date created')),
                ('date_updated', models.DateTimeField(blank=True, editable=False, verbose_name='Date updated')),
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('is_periodic', models.BooleanField(default=False, verbose_name='Periodic perform')),
                ('interval', models.IntegerField(blank=True, default=24, null=True, verbose_name='Cycle perform')),
                ('crontab', models.CharField(blank=True, max_length=128, null=True, verbose_name='Regularly perform')),
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4)),
                ('name', models.CharField(max_length=128, null=True, verbose_name='Name')),
                ('instant', models.BooleanField(default=False)),
                ('args', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='Args')),
                ('module', models.CharField(choices=[('shell', 'Shell'), ('win_shell', 'Powershell')], default='shell', max_length=128, null=True, verbose_name='Module')),
                ('chdir', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='Chdir')),
                ('timeout', models.IntegerField(default=60, verbose_name='Timeout (Seconds)')),
                ('type', models.CharField(choices=[('adhoc', 'Adhoc'), ('playbook', 'Playbook')], default='adhoc', max_length=128, verbose_name='Type')),
                ('runas', models.CharField(default='root', max_length=128, verbose_name='Runas')),
                ('runas_policy', models.CharField(choices=[('privileged_only', 'Privileged Only'), ('privileged_first', 'Privileged First'), ('skip', 'Skip')], default='skip', max_length=128, verbose_name='Runas policy')),
                ('use_parameter_define', models.BooleanField(default=False, verbose_name='Use Parameter Define')),
                ('parameters_define', models.JSONField(default=dict, verbose_name='Parameters define')),
                ('comment', models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='Comment')),
                ('version', models.IntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('creator', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('playbook', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ops.playbook', verbose_name='Playbook')),
            ],
            options={
                'verbose_name': 'historical job',
                'verbose_name_plural': 'historical jobs',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]