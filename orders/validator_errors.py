from rest_framework import status
from rest_framework.exceptions import ValidationError


class NotStockError(ValidationError):
    ...
