import random

from .currency_converter import currency_converter


def test_currency_conversion() -> None:

    conv_rates = {
        "GBP": {"CNY": 9.24, "PHP": 75.00, "INR": 109.06},
        "CNY": {"GBP": 0.11, "PHP": 8.12, "INR": 11.81},
        "PHP": {"CNY": 0.12, "GBP": 0.01, "INR": 1.45},
        "INR": {"PHP": 0.69, "CNY": 0.09, "GBP": 0.01},
    }

    for from_curr in conv_rates:
        for to_curr, rate in conv_rates[from_curr].items():
            amount = random.uniform(0, 1000)
            converted_amount = currency_converter(
                amount=amount, from_currency=from_curr, to_currency=to_curr
            )
            assert converted_amount == amount * rate
