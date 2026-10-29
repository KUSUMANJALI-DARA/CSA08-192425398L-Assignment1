
from decimal import Decimal

# Constants: values that remain fixed
BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_STEP = Decimal("0.1")
FAT_ADJUSTMENT = Decimal("0.40")
SNF_STEP = Decimal("0.1")
SNF_ADJUSTMENT = Decimal("0.30")

# Variables: values related to a farmer's milk delivery
farmer_id = "F001"
litres = Decimal("10.5")
fat = Decimal("4.0")
snf = Decimal("8.7")
shift = "Morning"

# Display the values
print("Farmer ID:", farmer_id)
print("Milk quantity:", litres, "litres")
print("Fat percentage:", fat, "%")
print("SNF percentage:", snf, "%")
print("Shift:", shift)
print("Base rate: Rs.", BASE_RATE)
print("Base fat:", BASE_FAT, "%")
print("Base SNF:", BASE_SNF, "%")
print("Fat adjustment: Rs.", FAT_ADJUSTMENT)
print("SNF adjustment: Rs.", SNF_ADJUSTMENT)
