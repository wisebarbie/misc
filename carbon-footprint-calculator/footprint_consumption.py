import doctest
from unit_conversion import *


INCOMPLETE = -1


def online(daily_online_use):
    '''
    (num) -> float
    Metric tonnes of CO2E from computing, based on daily hours of online use

    Source for online use: How Bad Are Bananas
    55 g CO2E / hour

    >>> round(online(0), 4)
    0.0
    >>> round(online(3), 4)
    0.0603
    >>> round(online(6), 4)
    0.1205
    '''
    online_result = kg_to_tonnes(daily_to_annual(daily_online_use * 55))/1000
    return online_result


def phone(daily_phone_use):
    '''
    (num) -> float
    Metric tonnes of CO2E from computing, based on daily hours of phone use

    Source for phone use: How Bad Are Bananas
    1250 kg CO2E for a year of 1 hour a day

    >>> round(phone(0), 4)
    0.0
    >>> round(phone(3), 4)
    3.75
    >>> round(phone(11), 4)
    13.75
    '''
    phone_result = kg_to_tonnes(daily_phone_use * 1250)
    return phone_result


def light_device(new_light_devices): 
    '''
    (num) -> float
    Metric tonnes of CO2E from computing, based on how many light devices you bought

    From: https://www.cnet.com/news/apple-iphone-x-environmental-report/
    Estimating 75kg for new small device

    >>> round(light_device(0), 4)
    0.0
    >>> round(light_device(2), 4)
    0.15
    >>> round(light_device(6), 4)
    0.45
    '''
    light_device_result = kg_to_tonnes(new_light_devices * 75)
    return light_device_result


def medium_device(new_medium_devices):
    '''
    (num) -> float
    Metric tonnes of CO2E from computing, based on how many medium devices you bought

    Source for new devices: How Bad Are Bananas
    200kg: new laptop

    >>> round(medium_device(0), 4)
    0.0
    >>> round(medium_device(4), 4)
    0.8
    >>> round(medium_device(1), 4)
    0.2
    '''
    medium_device_result = kg_to_tonnes(new_medium_devices * 200)
    return medium_device_result


def heavy_device(new_heavy_devices):
    '''
    (num) -> float
    Metric tonnes of CO2E from computing, based on how many heavy devices you bought

    Source for new devices: How Bad Are Bananas
    800kg: new workstation

    >>> round(heavy_device(0), 4)
    0.0
    >>> round(heavy_device(1), 4)
    0.8
    >>> round(heavy_device(3), 4)
    2.4
    '''
    heavy_device_result = kg_to_tonnes(new_heavy_devices * 800)
    return heavy_device_result


def fp_of_computing(daily_online_use, daily_phone_use, new_light_devices, new_medium_devices, new_heavy_devices):
    '''(num, num) -> float

    Metric tonnes of CO2E from computing, based on daily hours of online & phone use, and how many small (phone/tablet/etc) & large (laptop) & workstation devices you bought.

    Source for online use: How Bad Are Bananas
        55 g CO2E / hour

    Source for phone use: How Bad Are Bananas
        1250 kg CO2E for a year of 1 hour a day

    Source for new devices: How Bad Are Bananas
        200kg: new laptop
        800kg: new workstation
        And from: https://www.cnet.com/news/apple-iphone-x-environmental-report/
        I'm estimating 75kg: new small device

    >>> fp_of_computing(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_computing(6, 0, 0, 0, 0), 4)
    0.1205
    >>> round(fp_of_computing(0, 1, 0, 0, 0), 4)
    1.25
    >>> fp_of_computing(0, 0, 1, 0, 0)
    0.075
    >>> fp_of_computing(0, 0, 0, 1, 0)
    0.2
    >>> fp_of_computing(0, 0, 0, 0, 1)
    0.8
    >>> round(fp_of_computing(4, 2, 2, 1, 1), 4)
    3.7304
    '''
    # Calculate annual CO2E tonnes for each technological use
    v = online(daily_online_use)
    w = phone(daily_phone_use)
    x = light_device(new_light_devices)
    y = medium_device(new_medium_devices)
    z = heavy_device(new_heavy_devices) 
    # Sum annual CO2E tonnes for all technological uses
    CO2E = v + w + x + y + z 
    return CO2E


def vegan():
    '''
    () -> float
    Approximate annual CO2E footprint in metric tonnes from a vegan diet.

    Based on https://link.springer.com/article/10.1007%2Fs10584-014-1169-1
    A vegan diet is 2.89 kg CO2E / day in the UK.

    >>> round(vegan(), 4)
    1.0556
    '''
    vegan_result = kg_to_tonnes(daily_to_annual(2.89))
    return vegan_result


def meat(daily_g_meat):
    '''
    (num) -> float
    Approximate annual CO2E footprint in metric tonnes based on daily consumption of meat in grams.

    Based on https://link.springer.com/article/10.1007%2Fs10584-014-1169-1
    Approximately 0.0268 kgCO2E/day per gram of meat eaten.

    >>> round(meat(0), 4)
    0.0
    >>> round(meat(58), 4)
    0.5677
    >>> round(meat(120), 4)
    1.1746
    '''
    meat_result = kg_to_tonnes((daily_to_annual(daily_g_meat) * 26.8)/1000)
    return meat_result


def milk(daily_L_milk):
    '''
    (num) -> float
    Approximate annual CO2E footprint in metric tonnes based on daily consumption of milk in litres.

    Based on How Bad Are Bananas:
    1 pint of milk (2.7 litres) -> 723 g CO2E 
    ---> 1 litre of milk: 0.2677777 kg of CO2E
    
    >>> round(milk(0), 4)
    0.0
    >>> round(milk(1), 4)
    0.0978
    >>> round(milk(4), 4)
    0.3912
    '''
    milk_result = kg_to_tonnes((daily_to_annual(daily_L_milk) * 267.7777)/1000)
    return milk_result


def cheese(daily_g_cheese):
    '''
    (num) -> float
    Approximate annual CO2E footprint in metric tonnes based on daily consumption of cheese in grams.

    Based on How Bad Are Bananas:
    1 kg of hard cheese -> 12 kg CO2E 
    ---> 1 g cheese is 12 g CO2E -> 0.012 kg CO2E

    >>> round(cheese(0), 4)
    0.0
    >>> round(cheese(11), 4)
    0.0482
    >>> round(cheese(27), 4)
    0.1183
    '''
    cheese_result = kg_to_tonnes((daily_to_annual(daily_g_cheese) * 12)/1000)
    return cheese_result


def eggs(daily_num_eggs):
    '''
    (num) -> float
    Approximate annual CO2E footprint in metric tonnes based on daily consumption of eggs.

    Based on How Bad Are Bananas:
    12 eggs -> 3.6 kg CO2E 
    ---> 0.3 kg CO2E per egg

    >>> round(eggs(0), 4)
    0.0
    >>> round(eggs(2), 4)
    0.2191
    >>> round(eggs(5), 4)
    0.5479
    '''
    eggs_result = kg_to_tonnes((daily_to_annual(daily_num_eggs) * 300)/1000)
    return eggs_result


def fp_of_diet(daily_g_meat, daily_g_cheese, daily_L_milk, daily_num_eggs):
    '''
    (num, num, num, num) -> flt
    Approximate annual CO2E footprint in metric tonnes, from diet, based on daily consumption of meat in grams, cheese in grams, milk in litres, and eggs.

    Based on https://link.springer.com/article/10.1007%2Fs10584-014-1169-1
    A vegan diet is 2.89 kg CO2E / day in the UK.
    I infer approximately 0.0268 kgCO2E/day per gram of meat eaten.

    This calculation misses forms of dairy that are not milk or cheese, such as ice cream, yogourt, etc.

    From How Bad Are Bananas:
        1 pint of milk (2.7 litres) -> 723 g CO2E 
                ---> 1 litre of milk: 0.2677777 kg of CO2E
        1 kg of hard cheese -> 12 kg CO2E 
                ---> 1 g cheese is 12 g CO2E -> 0.012 kg CO2E
        12 eggs -> 3.6 kg CO2E 
                ---> 0.3 kg CO2E per egg

    >>> round(fp_of_diet(0, 0, 0, 0), 4) # vegan
    1.0556
    >>> round(fp_of_diet(0, 0, 0, 1), 4) # 1 egg
    1.1651
    >>> round(fp_of_diet(0, 0, 1, 0), 4) # 1 L milk
    1.1534
    >>> round(fp_of_diet(0, 0, 1, 1), 4) # egg and milk
    1.2629
    >>> round(fp_of_diet(0, 10, 0, 0), 4) # cheeese
    1.0994
    >>> round(fp_of_diet(0, 293.52, 1, 1), 4) # egg and milk and cheese
    2.5494
    >>> round(fp_of_diet(25, 0, 0, 0), 4) # meat
    1.3003
    >>> round(fp_of_diet(25, 293.52, 1, 1), 4) 
    2.7941
    >>> round(fp_of_diet(126, 293.52, 1, 1), 4)
    3.7827
    '''
    # Calculate annual CO2E tonnes for each type of food consumption
    a = vegan()
    b = meat(daily_g_meat)
    c = milk(daily_L_milk)
    d = cheese(daily_g_cheese)
    e = eggs(daily_num_eggs)
    # Sum annual CO2E tonnes for all types of food consumption
    C02E = a + b + c + d + e
    return C02E


if __name__ == '__main__':
    doctest.testmod()

