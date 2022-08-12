# Generated by Django 4.1 on 2022-08-12 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('CVV', models.IntegerField()),
                ('Fecha_otor', models.DateTimeField()),
                ('Fecha_exp', models.DateTimeField()),
                ('tipo_tarjeta', models.TextField()),
                ('marca', models.TextField()),
                ('client_cuenta', models.IntegerField()),
            ],
        ),
    ]