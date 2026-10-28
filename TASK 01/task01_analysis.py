
from decimal import Decimal

# Named constants
BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_STEP = Decimal("0.1")
FAT_ADJUSTMENT = Decimal("0.40")
SNF_STEP = Decimal("0.1")
SNF_ADJUSTMENT = Decimal("0.30")

MIN_FAT = Decimal("2.0")
MAX_FAT = Decimal("7.0")

# Sample farmer entry
farmer_id = "F001"
litres = Decimal("10.5")
fat = Decimal("4.0")
snf = Decimal("8.7")
shift = "Morning"

# Validate the entry
if litres <= 0:
    raise ValueError("Milk quantity must be positive")

if not MIN_FAT <= fat <= MAX_FAT:
    raise ValueError("Fat percentage is outside the allowed range")

# Calculate rate and payment
fat_steps = round((fat - BASE_FAT) / FAT_STEP)
snf_steps = round((snf - BASE_SNF) / SNF_STEP)

rate = BASE_RATE + (
    fat_steps * FAT_ADJUSTMENT
) + (
    snf_steps * SNF_ADJUSTMENT
)

amount = (litres * rate).quantize(Decimal("0.01"))

print("Farmer ID:", farmer_id)
print("Shift:", shift)
print("Milk quantity:", litres, "litres")
print("Fat:", fat, "%")
print("SNF:", snf, "%")
print("Rate per litre: Rs.", rate)
print("Payment amount: Rs.", amount)
