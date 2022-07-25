import datetime as dt
from dataclasses import dataclass

from django.core.exceptions import ValidationError


@dataclass()
class MinMaxYearValueValidators:
    MIN_YEAR: int = 0
    max_year: int = dt.datetime.now().year

    def __call__(self, val):
        if not self.MIN_YEAR < val < self.max_year:
            raise ValidationError(
                f'Значение года должно находится'
                f' в диапазоне от {self.MIN_YEAR} до {self.max_year}')
