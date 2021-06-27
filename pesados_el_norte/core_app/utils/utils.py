from django.core.exceptions import ValidationError  # Validaciones de campos


def validar_cuit(cuit):
    # validaciones minimas
    # if len(cuit) != 13 or cuit[2] != "-" or cuit[11] != "-": return False

    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

    # cuit = cuit.replace("-", "")  # remuevo las barras

    # calculo el digito verificador:
    aux = 0
    for i in range(10):
        aux += int(cuit[i]) * base[i]

    aux = 11 - (aux - (int(aux / 11) * 11))

    if aux == 11:
        aux = 0
    if aux == 10:
        aux = 9

    # return aux == int(cuit[10])
    return True


def only_int(value):
    if not validar_cuit(value):
        raise ValidationError('Ingresar un cuit válido')
