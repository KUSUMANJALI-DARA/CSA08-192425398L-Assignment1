
from decimal import Decimal
import milkrate

farmer_id = "F001"
litres = Decimal("10.5")
fat = Decimal("4.0")
snf = Decimal("8.7")

rate = milkrate.rate_per_litre(fat, snf)
amount = milkrate.payout(litres, fat, snf)

print("Farmer ID:", farmer_id)
print("Rate per litre: Rs.", rate)
print("Payment amount: Rs.", amount)
