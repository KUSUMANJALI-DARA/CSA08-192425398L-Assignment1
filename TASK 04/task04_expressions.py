
from decimal import Decimal

BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_STEP = Decimal("0.1")
FAT_ADJUSTMENT = Decimal("0.40")
SNF_STEP = Decimal("0.1")
SNF_ADJUSTMENT = Decimal("0.30")

farmer_id = "F001"
litres = Decimal("10.5")
fat = Decimal("4.2")
snf = Decimal("8.7")

# Calculate the number of fat and SNF steps
fat_steps = round((fat - BASE_FAT) / FAT_STEP)
snf_steps = round((snf - BASE_SNF) / SNF_STEP)

# Calculate rate and payment
rate = BASE_RATE + fat_steps * FAT_ADJUSTMENT + snf_steps * SNF_ADJUSTMENT
amount = (litres * rate).quantize(Decimal("0.01"))

print("Farmer ID:", farmer_id)
print("Fat steps:", fat_steps)
print("SNF steps:", snf_steps)
print("Rate per litre: Rs.", rate)
print("Payment amount: Rs.", amount)
