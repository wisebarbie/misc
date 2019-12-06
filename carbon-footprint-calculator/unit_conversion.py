import doctest


INCOMPLETE = -1


POUND_IN_KG = 0.45359237
KM_IN_MILES = 0.621371
DAYS_IN_YEAR = 365.2425


def kg_to_tonnes(kg):
    '''(num) -> float
    Convert mass in kg to in metric tonnes. 1000 kg = 1 tonne.
    >>> kg_to_tonnes(0)
    0.0
    >>> round(kg_to_tonnes(723), 4)
    0.723
    >>> round(kg_to_tonnes(0.5), 4)
    0.0005
    '''
    tonnes = kg/1000
    return tonnes


def pound_to_kg(lbs):
    '''(num) -> float
    Convert lbs to kg. 1 lbs is 0.453592 kg.
    >>> pound_to_kg(0)
    0.0
    >>> round(pound_to_kg(1), 4)
    0.4536
    >>> round(pound_to_kg(23), 4)
    10.4326
    '''
    kg = lbs * 0.453592
    return kg 


def km_to_miles(km):
    '''(num) -> float
    Convert km to miles.
    >>> km_to_miles(0)
    0.0
    >>> round(km_to_miles(100), 4)
    62.1371
    >>> round(km_to_miles(5), 4)
    3.1069
    '''
    miles = km * KM_IN_MILES
    return miles


def daily_to_annual(daily_value):
    '''(num) -> float
    Convert a daily_value to an annual value, 
    using number of days in Gregorian year (365.2425 days).
    >>> daily_to_annual(0)
    0.0
    >>> round(daily_to_annual(1), 4)
    365.2425
    >>> round(daily_to_annual(1000), 4)
    365242.5
    '''
    days = daily_value * DAYS_IN_YEAR
    return days


def weekly_to_annual(w):
    '''(num) -> num
    Convert a weekly amount into an annual
    amount assuming a Gregorian year of 365.2425 days.

    >>> weekly_to_annual(0)
    0.0
    >>> round(weekly_to_annual(1), 4)
    52.1775
    >>> round(weekly_to_annual(1.25), 4)
    65.2219
    '''
    weeks = w * 52.1775
    return weeks


def annual_to_daily(annual_value):
    '''(num) -> float
    Convert a annual_value to a daily value, using number of days in Gregorian year.
    >>> annual_to_daily(0)
    0.0
    >>> annual_to_daily(365.2425)
    1.0
    >>> round(annual_to_daily(356), 4)
    0.9747
    '''
    years = annual_value / DAYS_IN_YEAR
    return years


def pound_to_tonnes(lbs):
     '''(num) -> float
    Convert lbs to tonnes. 1 lbs is 0.000453592 tonnes
    >>> pound_to_tonnes(0)
    0.0
    >>> round(pound_to_tonnes(1), 4)
    0.0005
    >>> round(pound_to_tonnes(23), 4)
    0.0104
    '''
     value = kg_to_tonnes(pound_to_kg(lbs))
     return value


if __name__ == '__main__':
    doctest.testmod()
