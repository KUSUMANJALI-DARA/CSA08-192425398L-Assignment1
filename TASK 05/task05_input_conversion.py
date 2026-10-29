
from decimal import Decimal, InvalidOperation

# Read farmer details
farmer_id = input("Enter Farmer ID: ").strip()
shift = input("Enter shift (Morning/Evening): ").strip()

try:
    litres_text = input("Enter milk quantity in litres: ").strip()
    fat_text = input("Enter fat percentage: ").strip()
    snf_text = input("Enter SNF percentage: ").strip()

    litres = Decimal(litres_text)
    fat = Decimal(fat_text)
    snf = Decimal(snf_text)

    if not farmer_id:
        raise ValueError("Farmer ID cannot be empty")
    if shift.lower() not in ("morning", "evening"):
        raise ValueError("Shift must be Morning or Evening")
    if litres <= 0:
        raise ValueError("Milk quantity must be positive")
    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0 and 7.0")
    if not fat.is_finite() or not snf.is_finite() or not litres.is_finite():
        raise ValueError("Enter valid finite numbers")
    if snf <= 0:
        raise ValueError("SNF must be positive")

    # Calculate payment
    base_rate = Decimal("30.00")
    fat_steps = (fat - Decimal("3.5")) / Decimal("0.1")
    snf_steps = (snf - Decimal("8.5")) / Decimal("0.1")

    rate = base_rate + fat_steps * Decimal("0.40") + snf_steps * Decimal("0.30")
    amount = (litres * rate).quantize(Decimal("0.01"))

    print("\n--- Milk Payment Details ---")
    print(f"{'Farmer ID:':<22}{farmer_id}")
    print(f"{'Shift:':<22}{shift.title()}")
    print(f"{'Quantity (litres):':<22}{litres:>8}")
    print(f"{'Fat (%):':<22}{fat:>8}")
    print(f"{'SNF (%):':<22}{snf:>8}")
    print(f"{'Rate per litre (Rs.):':<22}{rate:>8.2f}")
    print(f"{'Payment (Rs.):':<22}{amount:>8.2f}")

except (InvalidOperation, ValueError) as error:
    print("Invalid input:", error)
