# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-10 08:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('action1', otree.db.models.StringField(choices=[('U', 'U'), ('M', 'M'), ('D', 'D')], max_length=10000, null=True)),
                ('action2', otree.db.models.StringField(choices=[('L', 'L'), ('M', 'M'), ('R', 'R')], max_length=10000, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asymmetric_pd_group', to='otree.Session')),
            ],
            options={
                'db_table': 'asymmetric_PD_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('my_id', otree.db.models.PositiveIntegerField(null=True)),
                ('interaction_number', otree.db.models.IntegerField(null=True)),
                ('round_in_interaction', otree.db.models.PositiveIntegerField(null=True)),
                ('treatment', otree.db.models.StringField(max_length=10000, null=True)),
                ('action', otree.db.models.StringField(max_length=10000, null=True)),
                ('other_action', otree.db.models.StringField(max_length=10000, null=True)),
                ('belief1', otree.db.models.IntegerField(null=True)),
                ('belief2', otree.db.models.IntegerField(null=True)),
                ('belief3', otree.db.models.IntegerField(null=True)),
                ('partner_id', otree.db.models.PositiveIntegerField(null=True)),
                ('potential_payoff', otree.db.models.CurrencyField(null=True)),
                ('other_payoff', otree.db.models.CurrencyField(null=True)),
                ('cum_payoff', otree.db.models.CurrencyField(null=True)),
                ('random_number', otree.db.models.PositiveIntegerField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asymmetric_PD.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asymmetric_pd_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asymmetric_pd_player', to='otree.Session')),
            ],
            options={
                'db_table': 'asymmetric_PD_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asymmetric_pd_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'asymmetric_PD_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asymmetric_PD.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asymmetric_PD.Subsession'),
        ),
    ]
