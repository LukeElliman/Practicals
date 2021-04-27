from Prac_08.UnreliableCar import UnreliableCar

def main():
    """Code to test unreliable car class"""
    bad_car = UnreliableCar("Bad_Car", 240, 20)
    good_car = UnreliableCar("Good_car", 240, 90)
    print(bad_car)
    print(good_car)
    for i in range(1, 21):
        print(f"Driving {i} kilometers")
        print(f"{bad_car.name:<8} drove {bad_car.drive(i)}km")
        print(f"{good_car.name} drove {good_car.drive(i)}km")
        print(good_car.odometer)

    print(f"{bad_car.name} odometer is {bad_car.odometer}km")
    print(f"{good_car.name} odometer is {good_car.odometer}km")

main()