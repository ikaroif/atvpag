# Generated by Django 5.1.3 on 2024-11-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id_carro', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=30)),
                ('ano', models.IntegerField()),
            ],
        ),
    ]
