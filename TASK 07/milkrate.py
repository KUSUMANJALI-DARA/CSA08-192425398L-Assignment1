
"""Module for calculating village milk payments."""

from decimal import Decimal

# Rate card constants
BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_STEP = Decimal("0.1")
FAT_ADJUSTMENT = Decimal("0.40")
SNF_STEP = Decimal("0.1")
SNF_ADJUSTMENT = Decimal("0.30")


def rate_per_litre(fat, snf):
    """Calculate and return the rate per litre."""
    fat_steps = round((fat - BASE_FAT) / FAT_STEP)
    snf_steps = round((snf - BASE_SNF) / SNF_STEP)

    return (
        BASE_RATE
        + fat_steps * FAT_ADJUSTMENT
        + snf_steps * SNF_ADJUSTMENT
    )


def payout(litres, fat, snf):
    """Calculate and return the payment rounded to two decimal places."""
    rate = rate_per_litre(fat, snf)
    return (litres * rate).quantize(Decimal("0.01"))


if __name__ == "__main__":
    # This example runs only when milkrate.py is executed directly.
    litres = Decimal("10.5")
    fat = Decimal("4.0")
    snf = Decimal("8.7")

    print("Rate per litre: Rs.", rate_per_litre(fat, snf))
    print("Payment amount: Rs.", payout(litres, fat, snf))
