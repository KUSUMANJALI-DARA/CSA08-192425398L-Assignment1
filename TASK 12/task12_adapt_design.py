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
    farmers = [
        ("F001", Decimal("10.5"), Decimal("4.0"), Decimal("8.7")),
        ("F002", Decimal("10"), Decimal("3.5"), Decimal("8.5")),
        ("F003", Decimal("5"), Decimal("4.0"), Decimal("9.0")),
    ]

    total_payment = Decimal("0.00")

    print("VILLAGE MILK CO-OPERATIVE")
    print("FARMER PAYMENT REPORT")

    for farmer_id, litres, fat, snf in farmers:
        rate, payment = calculate_payment(litres, fat, snf)

        total_payment += payment

        print("\nFarmer ID:", farmer_id)
        print("Milk Quantity:", litres, "litres")
        print("Fat:", fat, "%")
        print("SNF:", snf, "%")
        print("Rate per Litre: Rs.", rate)
        print("Payment: Rs.", payment)

    print("\nTotal Farmers:", len(farmers))
    print("Combined Payment: Rs.", total_payment)


if __name__ == "__main__":
    main()