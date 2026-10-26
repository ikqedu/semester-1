"""
Portfolio Task - Week 4

By submitting this code you are declaring that all work in this file,
other than any provided template code, was written and developed by
you independently.

Name:
"""

from typing import Literal

Currency = Literal["GBP", "CNY", "PHP", "INR"]

CONVERSION_RATES: dict[Currency, dict[Currency, float]] = {
    "GBP": {"CNY": 9.24, "PHP": 75.00, "INR": 109.06},
    "CNY": {"GBP": 0.11, "PHP": 8.12, "INR": 11.81},
    "PHP": {"CNY": 0.12, "GBP": 0.01, "INR": 1.45},
    "INR": {"PHP": 0.69, "CNY": 0.09, "GBP": 0.01},
}


def currency_converter(amount: float, from_currency: Currency, to_currency: Currency):
    """
    Converts an amount of one supported currency to another.
    Negative values return 0.0.
    Amount is expected to be numeric.
    Currency is expected to be supported.
    """

    if amount < 0:
        return 0.0

    return CONVERSION_RATES[from_currency][to_currency] * amount


# Submit only this file currency_converter.py with the completed function.

# Remove any additional code you may have added during development and testing.
