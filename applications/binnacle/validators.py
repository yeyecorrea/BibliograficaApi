from django.core.exceptions import ValidationError

# Validador para que el campo no sea mayor a 10
def validate_value(value):
    if value > 10:
        return value
    else:
        raise ValidationError("El valor no puede ser mayor a 10")