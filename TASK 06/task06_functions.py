
from decimal import Decimal

# Named constants
BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_STEP = Decimal("0.1")
FAT_ADJUSTMENT = Decimal("0.40")
SNF_STEP = Decimal("0.1")
SNF_ADJUSTMENT = Decimal("0.30")


def rate_per_litre(fat, snf):
    """Calculate the milk rate per litre from fat and SNF percentages."""
    fat_steps = round((fat - BASE_FAT) / FAT_STEP)
    snf_steps = round((snf - BASE_SNF) / SNF_STEP)

    rate = (
        BASE_RATE
        + fat_steps * FAT_ADJUSTMENT
        + snf_steps * SNF_ADJUSTMENT
    )
    return rate


def payout(litres, fat, snf):
    """Return the payment amount rounded to two decimal places."""
    rate = rate_per_litre(fat, snf)
    amount = (litres * rate).quantize(Decimal("0.01"))
    return amount


def ten_day_total(payments):
    """Return the total of all payments for ten days."""
    total = sum(payments, Decimal("0.00"))
    return total.quantize(Decimal("0.01"))


# Sample farmer details
farmer_id = "F001"
litres = Decimal("10.5")
fat = Decimal("4.0")
snf = Decimal("8.7")

# Call the functions
rate = rate_per_litre(fat, snf)
amount = payout(litres, fat, snf)

# Example ten-day payments
payments = [
    amount,
    Decimal("250.00"),
    Decimal("180.50")
]
total = ten_day_total(payments)

print("Farmer ID:", farmer_id)
print("Rate per litre: Rs.", rate)
print("Payment amount: Rs.", amount)
print("Ten-day total: Rs.", total)
