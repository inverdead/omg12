from math import sqrt
from obshee import consider_time


@consider_time
def dacha():
    print("Площадь участка")
    w = float(input("Ширина в футах"))
    l = float(input("Длина в футах"))
    SQFT_PER_ACRE = w*l
    print("Площадь в футах",SQFT_PER_ACRE)
    res=(SQFT_PER_ACRE/43560)
    print("Площадь в акрах", res)

@consider_time
def calculate_momentum(meters_height):
    meters_height = int(input("Введите высоту"))
    starting_speed = 0
    Gravity_thrust = 9.8
    starting_speed = sqrt(starting_speed ** 2)
    momentum = starting_speed + 2 * Gravity_thrust * meters_height
    return momentum


print("Какая задача? (1 или 2)")
pr = float(input())
if pr == 1:
    dacha()
if pr == 2:
    result = calculate_momentum(0)
    print(result)


