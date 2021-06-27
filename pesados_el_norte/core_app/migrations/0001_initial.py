# Generated by Django 3.1.12 on 2021-06-27 17:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pesados_el_norte.core_app.models.person
import pesados_el_norte.core_app.utils.utils
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('code', models.PositiveIntegerField(verbose_name='Cod Interno')),
                ('cuit', models.CharField(max_length=11, unique=True, validators=[pesados_el_norte.core_app.utils.utils.only_int], verbose_name='C.U.I.T.')),
                ('address', models.CharField(max_length=200, verbose_name='Direccion')),
                ('observations', models.CharField(blank=True, max_length=200, verbose_name='Observaciones')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Fecha')),
                ('prefix', models.PositiveIntegerField(verbose_name='Prefijo')),
                ('number', models.PositiveIntegerField(verbose_name='Numero')),
                ('amount', models.FloatField(verbose_name='Monto')),
                ('is_cash', models.BooleanField(default=False, verbose_name='Contado?')),
                ('approved', models.BooleanField(default=False, verbose_name='Aprobado?')),
                ('approved_at', models.DateTimeField(verbose_name='Fecha aprobacion')),
                ('observations', models.TextField(verbose_name='Observaciones')),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Aprobado por')),
                ('giver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='giver', to='core_app.person', verbose_name='Emisor')),
            ],
            options={
                'verbose_name': 'Comprobante',
                'verbose_name_plural': 'Comprobantes',
            },
        ),
        migrations.CreateModel(
            name='ReceiptType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('receipt_type', models.CharField(choices=[('Ventas/Recibo', 'Ventas / Recibo'), ('Compras', 'Compras'), ('Depositos', 'Depositos'), ('Gastos', 'Gastos'), ('Retiros', 'Retiros'), ('Redondeos', 'Redondeos'), ('Ingresos', 'Ingresos')], max_length=100, verbose_name='Tipo')),
                ('code', models.PositiveIntegerField(verbose_name='Codigo')),
                ('giver_type', models.CharField(choices=[('Client', pesados_el_norte.core_app.models.person.Client), ('Provider', pesados_el_norte.core_app.models.person.Provider)], max_length=100, verbose_name='Emisor')),
                ('receiver_type', models.CharField(choices=[('Client', pesados_el_norte.core_app.models.person.Client), ('Provider', pesados_el_norte.core_app.models.person.Provider)], max_length=100, verbose_name='Receptor')),
            ],
            options={
                'verbose_name': 'Tipo de Comprobante',
                'verbose_name_plural': 'Tipos de Comprobantes',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.person')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['name'],
            },
            bases=('core_app.person',),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core_app.person')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['name'],
            },
            bases=('core_app.person',),
        ),
        migrations.CreateModel(
            name='Retentions',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('amount', models.FloatField(verbose_name='Monto')),
                ('observations', models.TextField(verbose_name='Observaciones')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.PositiveIntegerField(verbose_name='Numero')),
                ('retention_type', models.CharField(choices=[('IVA', 'IVA'), ('IIBB', 'Ingresos Brutos'), ('Gcias', 'Ganancias')], max_length=100, verbose_name='Tipo de Retencion')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.receipt', verbose_name='Comprobante')),
            ],
            options={
                'verbose_name': 'Retencion',
                'verbose_name_plural': 'Retenciones',
                'ordering': ['date'],
            },
        ),
        migrations.AddField(
            model_name='receipt',
            name='receipt_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.receipttype', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='receiver', to='core_app.person', verbose_name='Receptor'),
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('amount', models.FloatField(verbose_name='Monto')),
                ('observations', models.TextField(verbose_name='Observaciones')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.PositiveIntegerField(verbose_name='Numero')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.receipt', verbose_name='Comprobante')),
            ],
            options={
                'verbose_name': 'Tarjeta de Credito',
                'verbose_name_plural': 'Tarjetas de Credito',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('amount', models.FloatField(verbose_name='Monto')),
                ('observations', models.TextField(verbose_name='Observaciones')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sign_date', models.DateField(default=datetime.date.today, verbose_name='Fecha Emision')),
                ('pay_date', models.DateField(default=datetime.date.today, verbose_name='Fecha Cobro')),
                ('number', models.PositiveIntegerField(verbose_name='Numero')),
                ('cuit', models.CharField(max_length=11, unique=True, validators=[pesados_el_norte.core_app.utils.utils.only_int], verbose_name='C.U.I.T.')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.receipt', verbose_name='Comprobante')),
            ],
            options={
                'verbose_name': 'Cheque',
                'verbose_name_plural': 'Cheques',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('amount', models.FloatField(verbose_name='Monto')),
                ('observations', models.TextField(verbose_name='Observaciones')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.receipt', verbose_name='Comprobante')),
            ],
            options={
                'verbose_name': 'Efectivo',
                'verbose_name_plural': 'Efectivo',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='BankTransferReceived',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('amount', models.FloatField(verbose_name='Monto')),
                ('observations', models.TextField(verbose_name='Observaciones')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.PositiveIntegerField(verbose_name='Numero')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.receipt', verbose_name='Comprobante')),
            ],
            options={
                'verbose_name': 'Transferencia Recibida',
                'verbose_name_plural': 'Transferencias Recibidas',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='BankTransferIssued',
            fields=[
                ('is_active', models.BooleanField(default=True, verbose_name='is active?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='last modified on')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('amount', models.FloatField(verbose_name='Monto')),
                ('observations', models.TextField(verbose_name='Observaciones')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.PositiveIntegerField(verbose_name='Numero')),
                ('account', models.CharField(choices=[('MACRO', 'Banco Macro'), ('PATAGONIA', 'Banco Patagonia')], max_length=100, verbose_name='Cuenta Propia Banco ')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Creado por')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core_app.receipt', verbose_name='Comprobante')),
            ],
            options={
                'verbose_name': 'Transferencia Emitida',
                'verbose_name_plural': 'Transferencias Emitidas',
                'ordering': ['date'],
            },
        ),
    ]
