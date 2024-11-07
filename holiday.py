












def hotel_cost(num_nights):
    num_nights * 2000
    print(num_nights)

def plane_cost(cost):
    if city_flight == london:
        cost = cost + 1000
    if city_flight == bangkok:
        cost = cost + 1500
    if city_flight == rome:
        cost = cost + 2500
    if city_flight == new_york:
        cost = cost + 6000
    else:
        exit

def car_rental(rental_days):
    rental_days * 40

def holiday_cost(plane_cost, hotel_cost, car_rental):
    holiday = {plane_cost} + {hotel_cost} + {car_rental}
    print(f"Your holiday will cost {holiday} dollars.")
'''
car_rental = 
plane_cost =
hotel_cost ='''



holiday2 = holiday_cost



city_flight = (input(f"What city will you be flying to? (london, bangkok, rome, new york)"))
                                    
num_nights = (input("How many nights will you be staying at the hotel? : "))

rental_days = (input("How many days will you hire the car for? : "))


hotel_cost()
