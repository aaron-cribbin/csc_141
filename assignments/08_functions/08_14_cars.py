# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

def car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

thought_car = car('ford', 'maverick', color='gray', year="2025")

print(thought_car)