import uuid
from django.db.models import CharField, PositiveIntegerField, UUIDField
from pesados_el_norte.core_app.models.basemodel import BaseModel
from pesados_el_norte.core_app.utils.utils import only_int


class Person(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = CharField(max_length=200, blank=False, verbose_name="Nombre")
    code = PositiveIntegerField(verbose_name="Cod Interno")
    cuit = CharField(
        validators=[only_int], max_length=11, unique=True, verbose_name="C.U.I.T."
    )
    address = CharField(max_length=200, blank=False, verbose_name="Direccion")
    observations = CharField(max_length=200, blank=True, verbose_name="Observaciones")

    def __str__(self):
        return f"{self.name.title}"

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Person, self).save(*args, **kwargs)

    class Meta:
        ordering = ["name"]
        verbose_name = "Persona"
        verbose_name_plural = "Personas"


class Client(Person):
    class Meta:
        ordering = ["name"]
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Provider(Person):
    class Meta:
        ordering = ["name"]
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
