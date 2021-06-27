import uuid
from django.db.models import BooleanField, CharField, FloatField, DateField, DateTimeField, PositiveIntegerField, \
    TextField, UUIDField, ForeignKey
from pesados_el_norte.core_app.models.basemodel import BaseModel
from pesados_el_norte.core_app.models.person import Client, Person, Provider
from pesados_el_norte.users.models import User


class ReceiptType(BaseModel):
    RECEIPT_TYPES = (
        ('Ventas/Recibo', 'Ventas / Recibo'),
        ('Compras', 'Compras'),
        ('Depositos', 'Depositos'),
        ('Gastos', 'Gastos'),
        ('Retiros', 'Retiros'),
        ('Redondeos', 'Redondeos'),
        ('Ingresos', 'Ingresos'),
    )
    PERSONS_TYPE = (
        ('Client', Client.__class__.name),
        ('Provider', Provider.__class__.name),
    )
    name = CharField(max_length=200, verbose_name='Nombre')
    receipt_type = CharField(blank=False, choices=RECEIPT_TYPES, verbose_name='Tipo')
    code = PositiveIntegerField(verbose_name='Codigo')
    giver_type = CharField(blank=False, choices=PERSONS_TYPE, verbose_name='Emisor')
    receiver_type = CharField(blank=False, choices=PERSONS_TYPE, verbose_name='Receptor')


class Receipt(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = DateField(verbose_name='Fecha')
    receipt_type = ForeignKey(ReceiptType, verbose_name='Tipo')
    prefix = PositiveIntegerField(verbose_name='Prefijo')
    number = PositiveIntegerField(verbose_name='Numero')
    amount = FloatField(verbose_name='Monto')
    is_cash = BooleanField(verbose_name='Contado?', default=False)
    giver = ForeignKey(Person, verbose_name='Emisor', null=True)
    receiver = ForeignKey(Person, verbose_name='Receptor', null=True)
    approved = BooleanField(verbose_name='Aprobado?', default=False)
    approved_by = ForeignKey(User, verbose_name='Aprobado por')
    approved_at = DateTimeField(verbose_name='Fecha aprobacion')
    observations = TextField(verbose_name='Observaciones')


# todo Falta el modelo del bonus receipt y migrar
