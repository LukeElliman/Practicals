"""
Electricity Bill 2.0
"""

TARIFF = {"11": 0.244618, "31": 0.136928, "45": 0.875391, "7": 0.298463, "57": 0.987654}
price_per_kWh = None

print("Electricity bill estimator 2.0")

tariff_choice = str(input("Which tariff 7, 11, 31, 45, 57: "))
while tariff_choice not in TARIFF:
    print("Not a valid tariff")
    tariff_choice = str(input("Which tariff 7, 11, 31, 45, 57: "))
price_per_kWh = TARIFF[tariff_choice]
daily_use_kWh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))


estimated_bill = (price_per_kWh * float(daily_use_kWh) * int(billing_days))
print("The estimated bill is: $" + "{:.2f}".format(estimated_bill))