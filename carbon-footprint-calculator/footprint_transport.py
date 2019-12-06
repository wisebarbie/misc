import doctest
from unit_conversion import *


INCOMPLETE = -1


def fp_from_driving(annual_km_driven):
    '''
    (num) -> flt
    Approximate CO2E footprint for one year of driving, based on total km driven.
    Result in metric tonnes.
    Source: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852
    "D.) Multiply total yearly mileage by .79 (for pounds)"

    >>> fp_from_driving(0)
    0.0
    >>> round(fp_from_driving(100), 4)
    0.0223
    >>> round(fp_from_driving(1234), 4)
    0.2748
    '''
    CO2E = kg_to_tonnes(pound_to_kg(0.79 * (km_to_miles(annual_km_driven))))
    return CO2E


def fp_from_taxi_uber(weekly_uber_rides):
    '''(num) -> flt
    Estimate in metric tonnes of CO2E the annual footprint from a given
    number of weekly uber/taxi/etc rides.

    Source: https://www.mapc.org/resource-library/the-growing-carbon-footprint-of-ride-hailing-in-massachusetts/
        81 million trips -> 100,000 metric tonnes

    >>> fp_from_taxi_uber(0)
    0.0
    >>> round(fp_from_taxi_uber(10), 4)
    0.6442
    >>> round(fp_from_taxi_uber(25), 4)
    1.6104
    '''
    CO2E = weekly_to_annual((weekly_uber_rides * 100000))/81000000
    return CO2E


def fp_from_transit(weekly_bus_trips, weekly_rail_trips):
    '''
    (num, num) -> flt
    Annual CO2E tonnes from public transit based on number of weekly bus
    rides and weekly rail (metro/commuter train) rides.

    Source: https://en.wikipedia.org/wiki/Transportation_in_Montreal
    The average amount of time people spend commuting with public transit in Montreal, for example to and from work, on a weekday is 87 min. 29.% of public transit riders, ride for more than 2 hours every day. The average amount of time people wait at a stop or station for public transit is 14 min, while 17% of riders wait for over 20 minutes on average every day. The average distance people usually ride in a single trip with public transit is 7.7 km, while 17% travel for over 12 km in a single direction.[28]
   
    Source: How Bad Are Bananas
        A mile by bus: 150g CO2E
        A mile by subway train: 160g CO2E for London Underground

    >>> fp_from_transit(0, 0)
    0.0
    >>> round(fp_from_transit(1, 0), 4)
    0.0374
    >>> round(fp_from_transit(0, 1), 4)
    0.0399
    >>> round(fp_from_transit(10, 2), 4)
    0.4544
    '''
    # Calculate annual CO2E tonnes for weekly bus rides
    x = (weekly_to_annual(kg_to_tonnes(((km_to_miles(weekly_bus_trips * 7.7)) * 150)/1000)))
    # Calculate annual CO2E tonnes for weekly train rides
    y = (weekly_to_annual(kg_to_tonnes(((km_to_miles(weekly_rail_trips * 7.7)) * 160)/1000)))
    # Sum annual CO2E tonnes for weekly bus rides and weekly train rides 
    CO2E = x + y
    return CO2E


def fp_of_transportation(weekly_bus_rides, weekly_rail_rides, weekly_uber_rides, weekly_km_driven):
    '''(num, num, num, num) -> flt
    Estimate in tonnes of CO2E the footprint of weekly transportation given
    specified annual footprint in tonnes of CO2E from diet.

    >>> fp_of_transportation(0, 0, 0, 0)
    0.0
    >>> round(fp_of_transportation(2, 2, 1, 10), 4)
    0.3354
    >>> round(fp_of_transportation(1, 2, 3, 4), 4)
    0.3571
    '''
    # Calculate annual CO2E tonnes for public transit
    f = fp_from_transit(weekly_bus_rides, weekly_rail_rides) 
    # Calculate annual CO2E tonnes for uber rides
    g = fp_from_taxi_uber(weekly_uber_rides)
    # Calculate annual CO2E tonnes for driving 
    h = fp_from_driving(weekly_to_annual(weekly_km_driven))
    # Sum annual CO2E tonnes for all modes of transport mentioned
    CO2E = f + g + h
    return CO2E


def short_flight(annual_short_flights):
    '''
    (num) -> float
    Approximate CO2E footprint in metric tonnes for annual short flights.

    Source for flights: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852 --- in lbs
    Multiply the number of flights--4 hours or less--by 1,100 lbs

    >>> round(short_flight(0), 4)
    0.0
    >>> round(short_flight(17), 4)
    8.4822
    >>> round(short_flight(30), 4)
    14.9685
    '''
    short_flight_result = kg_to_tonnes(pound_to_kg(annual_short_flights * 1100))
    return short_flight_result


def long_flight(annual_long_flights):
    '''
    (num) -> float
    Approximate CO2E footprint in metric tonnes for annual long flights.

    Source for flights: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852 --- in lbs
    Multiply the number of flights--4 hours or more--by 4,400 lbs

    >>> round(long_flight(0), 4)
    0.0
    >>> round(long_flight(2), 4)
    3.9916
    >>> round(long_flight(4), 4)
    7.9832
    '''
    long_flight_result = kg_to_tonnes(pound_to_kg(annual_long_flights * 4400))
    return long_flight_result


def train(annual_train):
    '''
    (num) -> float
    Approximate CO2E footprint in metric tonnes for annual train rides.

    Source for trains: https://media.viarail.ca/sites/default/files/publications/SustainableMobilityReport2016_EN_FINAL.pdf
    137,007 tCO2E from all of Via Rail, 3974000 riders
    -> 34.45 kg CO2E

    >>> round(train(0), 4)
    0.0
    >>> round(train(5), 4)
    0.1722
    >>> round(train(21), 4)
    0.7235
    '''
    train_result = kg_to_tonnes(annual_train * 34.45)
    return train_result


def coach(annual_coach):
    '''
    (num) -> float
    Approximate CO2E footprint in metric tonnes for annual coach rides.

    Source for buses: How Bad Are Bananas
    66kg CO2E for ROUND TRIP coach bus ride from NYC to Niagara Falls

    >>> round(coach(0), 4)
    0.0
    >>> round(coach(3), 4)
    0.099
    >>> round(coach(7), 4)
    0.231
    '''
    coach_result = kg_to_tonnes(annual_coach * 33)
    return coach_result


def hotel(annual_hotels):
    '''
    (num) -> float
    Approximate CO2E footprint in metric tonnes for annual hotel stays.

    Source for hotels: How Bad Are Bananas
    270 g CO2E for every dollar spent

    >>> round(hotel(0), 4)
    0.0
    >>> round(hotel(4), 4)
    0.0011
    >>> round(hotel(38), 4)
    0.0103
    '''
    hotel_result = kg_to_tonnes(annual_hotels * 270)/1000
    return hotel_result


def fp_of_travel(annual_long_flights, annual_short_flights, annual_train, annual_coach, annual_hotels):
    '''(num, num, num, num, num) -> float
    Approximate CO2E footprint in metric tonnes for annual travel, based on number of long flights (>4 h), short flights (<4), intercity train rides, intercity coach bus rides, and spending at hotels.

    Source for flights: https://www.forbes.com/2008/04/15/green-carbon-living-forbeslife-cx_ls_0415carbon.html#1f3715d01852 --- in lbs
    "E.) Multiply the number of flights--4 hours or less--by 1,100 lbs
    F.) Multiply the number of flights--4 hours or more--by 4,400 libs"

    Source for trains: https://media.viarail.ca/sites/default/files/publications/SustainableMobilityReport2016_EN_FINAL.pdf
    137,007 tCO2E from all of Via Rail, 3974000 riders
        -> 34.45 kg CO2E

    Source for buses: How Bad Are Bananas
        66kg CO2E for ROUND TRIP coach bus ride from NYC to Niagara Falls
        I'm going to just assume that's an average length trip, because better data not readily avialible.

    Source for hotels: How Bad Are Bananas
        270 g CO2E for every dollar spent

    >>> fp_of_travel(0, 0, 0, 0, 0)
    0.0
    >>> round(fp_of_travel(0, 1, 0, 0, 0), 4) # short flight
    0.499
    >>> round(fp_of_travel(1, 0, 0, 0, 0), 4) # long flight
    1.9958
    >>> round(fp_of_travel(2, 2, 0, 0, 0), 4) # some flights
    4.9895
    >>> round(fp_of_travel(0, 0, 1, 0, 0), 4) # train
    0.0345
    >>> round(fp_of_travel(0, 0, 0, 1, 0), 4) # bus
    0.033
    >>> round(fp_of_travel(0, 0, 0, 0, 100), 4) # hotel
    0.027
    >>> round(fp_of_travel(6, 4, 24, 2, 2000), 4) # together
    15.4034
    >>> round(fp_of_travel(1, 2, 3, 4, 5), 4) # together
    3.2304
    '''
    # Calculate annual CO2E tonnes for each aspect of travel
    a = short_flight(annual_short_flights)
    b = long_flight(annual_long_flights)
    c = train(annual_train)
    d = coach(annual_coach)
    e = hotel(annual_hotels)
    # Sum annual CO2E tonnes for all aspects of travel
    CO2E = a + b + c + d + e
    return CO2E


if __name__ == '__main__':
    doctest.testmod()