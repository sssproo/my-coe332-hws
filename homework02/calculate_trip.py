import math
import json


def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    mars_radius = 3389.5
    lat1, lon1, lat2, lon2 = map(math.radians, [latitude_1, longitude_1, latitude_2, longitude_2])
    d_sigma = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1 - lon2)))
    return mars_radius * d_sigma


def main():
    latitude = 16.0
    longitude = 82.0
    cost = {'stony': 1, 'iron': 2, 'stony-iron': 3}
    with open("sites.json", 'r') as load_f:
        load_dict = json.load(load_f)
    n = len(load_dict['sites'])
    speed = 10.0
    time_cost = 0.0
    for i in range(n):
        distance = calc_gcd(latitude, longitude, load_dict['sites'][i]['latitude'], load_dict['sites'][i]['longitude'])
        travel_time_cost = distance / speed + cost[load_dict['sites'][i]['composition']]
        sample_time_cost = cost[load_dict['sites'][i]['composition']]
        time_cost += travel_time_cost + sample_time_cost
        print(
            f'leg = {i + 1}, time to travel = {round(travel_time_cost, 2)} hr, time to sample = {round(sample_time_cost, 2)} hr')
        latitude = load_dict['sites'][i]['latitude']
        longitude = load_dict['sites'][i]['longitude']
    print('================================================')
    print(f'number of legs = {n}, total time elapsed = {round(time_cost, 2)} hr')


if __name__ == '__main__':
    main()

