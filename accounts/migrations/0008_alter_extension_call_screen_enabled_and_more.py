# Generated by Django 4.0.4 on 2022-12-06 20:19

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0003_alter_defaultsetting_enabled_alter_domain_enabled_and_more'),
        ('accounts', '0007_alter_extension_missed_call_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extension',
            name='call_screen_enabled',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='false', max_length=8, verbose_name='Call Screen'),
        ),
        migrations.AlterField(
            model_name='extension',
            name='directory_exten_visible',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Directory Ext. Visible'),
        ),
        migrations.AlterField(
            model_name='extension',
            name='directory_visible',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Directory Visible'),
        ),
        migrations.AlterField(
            model_name='extension',
            name='do_not_disturb',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='false', max_length=8, verbose_name='Do Not Disturb'),
        ),
        migrations.AlterField(
            model_name='extension',
            name='enabled',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Enabled'),
        ),
        migrations.AlterField(
            model_name='extension',
            name='follow_me_enabled',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='false', max_length=8, verbose_name='Follow Me Enabled'),
        ),
        migrations.AlterField(
            model_name='extension',
            name='force_ping',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='false', max_length=8, verbose_name='Force Ping'),
        ),
        migrations.AlterField(
            model_name='extension',
            name='forward_all_enabled',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='false', max_length=8, verbose_name='Forward All Enabled'),
        ),
        migrations.AlterField(
            model_name='extension',
            name='forward_busy_enabled',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='false', max_length=8, verbose_name='Forward Busy Enabled'),
        ),
        migrations.AlterField(
            model_name='extension',
            name='forward_no_answer_enabled',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='false', max_length=8, verbose_name='Forward No Answer Enabled'),
        ),
        migrations.AlterField(
            model_name='extension',
            name='forward_user_not_registered_enabled',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='false', max_length=8, verbose_name='Forward Not Registered Enabled'),
        ),
        migrations.AlterField(
            model_name='extensionuser',
            name='default_user',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Default'),
        ),
        migrations.AlterField(
            model_name='gateway',
            name='enabled',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Enabled'),
        ),
        migrations.AlterField(
            model_name='gateway',
            name='register',
            field=models.CharField(choices=[('false', 'False'), ('true', 'True')], default='false', max_length=8, verbose_name='Register'),
        ),
        migrations.CreateModel(
            name='Bridge',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Bridge')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('destination', models.CharField(max_length=256, verbose_name='Destination')),
                ('enabled', models.CharField(choices=[('false', 'False'), ('true', 'True')], default='true', max_length=8, verbose_name='Enabled')),
                ('description', models.CharField(blank=True, max_length=64, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated')),
                ('synchronised', models.DateTimeField(blank=True, null=True, verbose_name='Synchronised')),
                ('updated_by', models.CharField(max_length=64, verbose_name='Updated by')),
                ('domain_id', models.ForeignKey(blank=True, db_column='domain_uuid', null=True, on_delete=django.db.models.deletion.CASCADE, to='tenants.domain', verbose_name='Domain')),
            ],
            options={
                'db_table': 'pbx_bridges',
            },
        ),
    ]
