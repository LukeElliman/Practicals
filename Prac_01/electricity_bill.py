TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
price_per_kWh = None

print("Electricity bill estimator 2.0")

tariff_choice = int(input("Which tariff? 11 or 31: "))
daily_use_kWh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

#Makes sure tariff choice is valid.
while price_per_kWh is None:
    if tariff_choice == int(11):
        price_per_kWh = TARIFF_11
    elif tariff_choice == int(31):
        price_per_kWh = TARIFF_31
    else:
        print("You did not enter a valid tariff")
        tariff_choice = int(input("Which tariff? 11 or 31: "))


estimated_bill = (price_per_kWh * float(daily_use_kWh) * int(billing_days))
print("The estimated bill is: $" + "{:.2f}".format(estimated_bill))