from decimal import Decimal
from django import forms

class PercentageField(forms.DecimalField):
    """
    A form field that displays a stored decimal as a percentage (e.g., 0.07 becomes 7).
    """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('min_value', 0)
        kwargs.setdefault('max_value', 100)
        kwargs.setdefault('max_digits', 5)
        kwargs.setdefault('decimal_places', 2)
        super().__init__(*args, **kwargs)

    def prepare_value(self, value):
        """Converts the internal decimal to a percentage for display."""
        if value is not None:
            return value * Decimal('100')
        return value

    def clean(self, value):
        """Converts the user's input percentage back to a decimal."""
        cleaned_value = super().clean(value)
        if cleaned_value is not None:
            return cleaned_value / Decimal('100')
        return None