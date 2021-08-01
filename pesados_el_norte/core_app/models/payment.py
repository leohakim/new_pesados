import uuid
import datetime

from django.db.models import (
    CharField,
    DateField,
    FloatField,
    ForeignKey,
    PositiveIntegerField,
    PROTECT,
    TextField,
    UUIDField,
)
from pesados_el_norte.core_app.models.basemodel import BaseModel
from pesados_el_norte.core_app.models.receipt import Receipt
from pesados_el_norte.users.models import User
from pesados_el_norte.core_app.utils.utils import only_int


class Payment(BaseModel):
    receipt = ForeignKey(Receipt, on_delete=PROTECT, verbose_name="Comprobante")
    date = DateField(default=datetime.date.today, verbose_name="Fecha")
    amount = FloatField(verbose_name="Monto")
    observations = TextField(verbose_name="Observaciones")
    created_by = ForeignKey(User, on_delete=PROTECT, verbose_name="Creado por")

    def __str__(self):
        return f"{self.receipt.date}"

    class Meta:
        abstract = True
        ordering = ["name"]
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"


class Cash(Payment):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"$ {self.amount}"

    class Meta:
        ordering = ["date"]
        verbose_name = "Efectivo"
        verbose_name_plural = "Efectivo"


class Check(Payment):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sign_date = DateField(default=datetime.date.today, verbose_name="Fecha Emision")
    pay_date = DateField(default=datetime.date.today, verbose_name="Fecha Cobro")
    number = PositiveIntegerField(verbose_name="Numero")
    cuit = CharField(
        validators=[only_int], max_length=11, unique=True, verbose_name="C.U.I.T."
    )

    class Meta:
        ordering = ["date"]
        verbose_name = "Cheque"
        verbose_name_plural = "Cheques"


class BankTransferReceived(Payment):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = PositiveIntegerField(verbose_name="Numero")

    class Meta:
        ordering = ["date"]
        verbose_name = "Transferencia Recibida"
        verbose_name_plural = "Transferencias Recibidas"


class BankTransferIssued(Payment):
    ACCOUNTS = (
        ("MACRO", "Banco Macro"),
        ("PATAGONIA", "Banco Patagonia"),
    )
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = PositiveIntegerField(verbose_name="Numero")
    account = CharField(
        blank=False,
        choices=ACCOUNTS,
        verbose_name="Cuenta Propia Banco ",
        max_length=100,
    )

    class Meta:
        ordering = ["date"]
        verbose_name = "Transferencia Emitida"
        verbose_name_plural = "Transferencias Emitidas"


class CreditCard(Payment):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = PositiveIntegerField(verbose_name="Numero")

    class Meta:
        ordering = ["date"]
        verbose_name = "Tarjeta de Credito"
        verbose_name_plural = "Tarjetas de Credito"


class DebitCard(Payment):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = PositiveIntegerField(verbose_name="Numero")

    class Meta:
        ordering = ["date"]
        verbose_name = "Tarjeta de Debito"
        verbose_name_plural = "Tarjetas de Debito"


class Retentions(Payment):
    RETENTIONS_TYPES = (
        ("IVA", "IVA"),
        ("IIBB", "Ingresos Brutos"),
        ("Gcias", "Ganancias"),
    )

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = PositiveIntegerField(verbose_name="Numero")
    retention_type = CharField(
        blank=False,
        choices=RETENTIONS_TYPES,
        verbose_name="Tipo de Retencion",
        max_length=100,
    )

    class Meta:
        ordering = ["date"]
        verbose_name = "Retencion"
        verbose_name_plural = "Retenciones"
