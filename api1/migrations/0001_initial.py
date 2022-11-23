# Generated by Django 4.1.3 on 2022-11-23 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_imovel', models.PositiveIntegerField(auto_created=True)),
                ('limite_de_hospedes', models.PositiveIntegerField()),
                ('quantidade_toilet', models.PositiveIntegerField()),
                ('pet_friendly', models.BooleanField()),
                ('tx_de_limpeza', models.DecimalField(decimal_places=2, max_digits=5)),
                ('data_de_ativacao', models.DateField(auto_now=True)),
                ('data_hora_de_criacao', models.DateTimeField(auto_now=True)),
                ('data_hora_de_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
