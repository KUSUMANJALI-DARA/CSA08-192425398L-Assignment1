
from decimal import Decimal

# Step 1: Define the rate constants
BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")
FAT_STEP = Decimal("0.1")
FAT_ADJUSTMENT = Decimal("0.40")
SNF_STEP = Decimal("0.1")
SNF_ADJUSTMENT = Decimal("0.30")


# Step 2: Define the calculation function
def calculate_payment(litres, fat, snf):
    """Calculate the milk rate and payment amount."""

    # Step 3: Calculate fat and SNF steps
    fat_steps = round((fat - BASE_FAT) / FAT_STEP)
    snf_steps = round((snf - BASE_SNF) / SNF_STEP)

    # Step 4: Calculate rate per litre
    rate = (
        BASE_RATE
        + fat_steps * FAT_ADJUSTMENT
        + snf_steps * SNF_ADJUSTMENT
    )

    # Step 5: Calculate the payment amount
    amount = (litres * rate).quantize(Decimal("0.01"))

    return rate, amount


# Step 6: Provide sample input
farmer_id = "F001"
litres = Decimal("10.5")
fat = Decimal("4.0")
snf = Decimal("8.7")

# Step 7: Call the function
rate, amount = calculate_payment(litres, fat, snf)

# Step 8: Display the results
print("Farmer ID:", farmer_id)
print("Milk quantity:", litres, "litres")
print("Fat:", fat, "%")
print("SNF:", snf, "%")
print("Rate per litre: Rs.", rate)
print("Payment amount: Rs.", amount)
