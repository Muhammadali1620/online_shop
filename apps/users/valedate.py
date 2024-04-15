from django.core.exceptions import ValidationError


def validate_phone_number(phone_number: str):
    if len(phone_number) != 13 or not phone_number.startswith('+998') or not phone_number[1:].isdigit():
        raise ValidationError('phone number is not valid')
 