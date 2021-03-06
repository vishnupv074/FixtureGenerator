# Generated by Django 3.0.7 on 2020-06-03 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(max_length=50, unique=True)),
                ('manager', models.CharField(max_length=50)),
                ('coach', models.CharField(max_length=50)),
                ('player1', models.CharField(max_length=20)),
                ('player2', models.CharField(max_length=20)),
                ('player3', models.CharField(max_length=20)),
                ('player4', models.CharField(max_length=20)),
                ('player5', models.CharField(max_length=20)),
                ('player6', models.CharField(max_length=20)),
                ('player7', models.CharField(max_length=20)),
                ('player8', models.CharField(max_length=20)),
                ('player9', models.CharField(max_length=20)),
                ('player10', models.CharField(max_length=20)),
                ('player11', models.CharField(max_length=20)),
                ('goals', models.IntegerField(null=True)),
                ('wins', models.IntegerField(null=True)),
                ('fails', models.IntegerField(null=True)),
                ('score', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team1', to='webapp.Teams')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team2', to='webapp.Teams')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='webapp.Venues')),
            ],
        ),
    ]
