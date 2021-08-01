from django.contrib import admin
from pesados_el_norte.core_app.models.person import Client, Provider
from pesados_el_norte.core_app.models.receipt import Receipt, ReceiptType
from pesados_el_norte.core_app.models.payment import (
    BankTransferIssued,
    BankTransferReceived,
    Cash,
    Check,
    Card,
    Retentions,
)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "code", "cuit"]
    search_fields = ["name"]


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "code", "cuit"]
    search_fields = ["name"]


@admin.register(ReceiptType)
class ReceiptTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "code", "giver_type", "receiver_type"]
    search_fields = ["name"]


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "date",
        "receipt_type",
        "prefix",
        "number",
        "amount",
        "is_cash",
        "giver",
        "receiver",
    ]
    search_fields = ["date"]


@admin.register(Cash)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ["id", "receipt", "date", "amount", "observations"]
    search_fields = ["date"]


@admin.register(Check)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "receipt",
        "date",
        "amount",
        "sign_date",
        "pay_date",
        "number",
        "cuit",
    ]
    search_fields = ["date"]


@admin.register(BankTransferReceived)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ["id", "receipt", "date", "amount", "number"]
    search_fields = ["date"]


@admin.register(BankTransferIssued)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ["id", "receipt", "date", "amount", "number"]
    search_fields = ["date"]


@admin.register(Card)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ["id", "type", "receipt", "date", "amount", "number"]
    search_fields = ["date"]


@admin.register(Retentions)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ["id", "retention_type", "receipt", "date", "amount", "number"]
    search_fields = ["date"]
