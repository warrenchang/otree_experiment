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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_info_asym_pd_group', to='otree.Session')),
            ],
            options={
                'db_table': 'payment_info_asym_PD_group',
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
                ('final_payment', otree.db.models.CurrencyField(null=True)),
                ('real_payoff_PD', otree.db.models.CurrencyField(null=True)),
                ('real_payoff_guess', otree.db.models.CurrencyField(null=True)),
                ('real_payoff_SP', otree.db.models.CurrencyField(null=True)),
                ('participation_fee', otree.db.models.CurrencyField(null=True)),
                ('role_SP', otree.db.models.IntegerField(null=True)),
                ('decision_SP', otree.db.models.IntegerField(null=True)),
                ('paying_game', otree.db.models.StringField(max_length=10000, null=True)),
                ('decision_number', otree.db.models.IntegerField(null=True)),
                ('UG_MAO', otree.db.models.IntegerField(null=True)),
                ('UG_offer', otree.db.models.IntegerField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment_info_asym_PD.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_info_asym_pd_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_info_asym_pd_player', to='otree.Session')),
            ],
            options={
                'db_table': 'payment_info_asym_PD_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_info_asym_pd_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'payment_info_asym_PD_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment_info_asym_PD.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment_info_asym_PD.Subsession'),
        ),
    ]