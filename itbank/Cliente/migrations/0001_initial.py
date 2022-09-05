# Generated by Django 4.1 on 2022-09-05 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI')),
                ('dob', models.TextField(blank=True, null=True)),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('iban', models.TextField()),
            ],
            options={
                'db_table': 'cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.TextField()),
                ('numero', models.IntegerField()),
                ('ciudad', models.TextField()),
                ('provincia', models.TextField()),
                ('pais', models.TextField()),
            ],
            options={
                'db_table': 'direcciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.TextField()),
                ('employee_surname', models.TextField()),
                ('employee_hire_date', models.TextField()),
                ('employee_dni', models.TextField(db_column='employee_DNI')),
                ('branch_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empleado',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Moviminetos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificacion', models.IntegerField()),
                ('nro_cuenta', models.IntegerField()),
                ('monto', models.IntegerField()),
                ('tipo_operacion', models.IntegerField()),
                ('hora', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'moviminetos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MTarjetas',
            fields=[
                ('credit_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_credito', models.TextField()),
            ],
            options={
                'db_table': 'm_tarjetas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('loan_id', models.AutoField(primary_key=True, serialize=False)),
                ('loan_type', models.TextField()),
                ('loan_date', models.TextField()),
                ('loan_total', models.IntegerField()),
                ('customer_id', models.IntegerField()),
            ],
            options={
                'db_table': 'prestamo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('branch_id', models.AutoField(primary_key=True, serialize=False)),
                ('branch_number', models.BinaryField()),
                ('branch_name', models.TextField()),
                ('branch_address_id', models.IntegerField()),
            ],
            options={
                'db_table': 'sucursal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('numero', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('cvv', models.IntegerField(db_column='CVV')),
                ('fecha_otorgamiento', models.TextField(blank=True, db_column='Fecha_Otorgamiento', null=True)),
                ('fecha_expiracion', models.TextField(blank=True, db_column='fecha_Expiracion', null=True)),
                ('tipo_tarjeta', models.TextField()),
            ],
            options={
                'db_table': 'tarjeta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tclien',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_des', models.TextField()),
            ],
            options={
                'db_table': 'Tclien',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TCuenta',
            fields=[
                ('cuenta_id', models.AutoField(primary_key=True, serialize=False)),
                ('descipcion', models.TextField()),
            ],
            options={
                'db_table': 'T_cuenta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.TextField()),
                ('Cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Cliente.cliente')),
                ('Cuenta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Cliente.cuenta')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
