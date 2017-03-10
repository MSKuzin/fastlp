# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 02:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(help_text='Host of this game', max_length=50)),
                ('start_time', models.DateTimeField(help_text='Start time of the game')),
                ('finish_time', models.DateTimeField(help_text='Finish time of the game')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_games', models.IntegerField(default=5, help_text='Number of games player has paid for')),
                ('price_of_game', models.CharField(choices=[('USD', '1 USD per game'), ('RUB', '30 RUB per game')], default='RUB', max_length=3)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(help_text="Player's nickname", max_length=50)),
                ('dota_id', models.CharField(help_text="Player's dota id", max_length=50)),
                ('misc_data', models.TextField(blank=True, help_text='Put here some information about how to reach this user, e.g. vk, steam, facebook, etc', verbose_name='Custom user data')),
            ],
        ),
        migrations.AddField(
            model_name='payment',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastlp.Player'),
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(help_text='All players in party for this game', to='fastlp.Player'),
        ),
    ]
