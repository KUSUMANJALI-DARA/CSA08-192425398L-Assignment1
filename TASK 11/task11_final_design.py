from decimal import Decimal

BASE_RATE = Decimal("30.00")
BASE_FAT = Decimal("3.5")
BASE_SNF = Decimal("8.5")

FAT_STEP = Decimal("0.1")
FAT_ADJUSTMENT = Decimal("0.40")

SNF_STEP = Decimal("0.1")
SNF_ADJUSTMENT = Decimal("0.30")


def calculate_payment(litres, fat, snf):
    fat_steps = (fat - BASE_FAT) / FAT_STEP
    snf_steps = (snf - BASE_SNF) / SNF_STEP

    rate = (
        BASE_RATE
        + fat_steps * FAT_ADJUSTMENT
        + snf_steps * SNF_ADJUSTMENT
    )

    amount = (litres * rate).quantize(Decimal("0.01"))

    return rate, amount


def main():
    farmer_id = "F001"
    litres = Decimal("10.5")
    fat = Decimal("4.0")
    snf = Decimal("8.7")

    rate, amount = calculate_payment(litres, fat, snf)

    print("Farmer ID:", farmer_id)
    print("Milk Quantity:", litres, "litres")
    print("Fat:", fat, "%")
    print("SNF:", snf, "%")
    print("Rate per Litre: Rs.", rate)
    print("Total Payment: Rs.", amount)


if __name__ == "__main__":
    main()