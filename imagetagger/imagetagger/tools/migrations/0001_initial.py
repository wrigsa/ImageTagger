# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-21 12:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tool_creator', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tool_team', to='users.Team')),
            ],
        ),
        migrations.CreateModel(
            name='ToolVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('positive', models.BooleanField(default=0)),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tool', to='tools.Tool')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='toolvote',
            unique_together=set([('tool', 'user')]),
        ),
    ]
