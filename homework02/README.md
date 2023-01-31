No One JSON
=

* This project is for COE332 homework 02.

* This purpose of this project is imagining you are operating a robotic vehicle on Mars and the task for today is to investigate five meteorite landing sites in Syrtis Major.

Installation
--
Install this project by cloning the repository, making the scripts executable, and adding them to your PATH. For example:

```
git clone ...
chmod ...
...
...

etc
```


Running the Code
--

This folder has two scripts:

* generate_sites


   * You can use this script to randomly generate latitude, longitude, and compositions for the five meteorite landing sites.
   * Generate five random pairs of latitudes (between 16.0 - 18.0 degrees North) and longitudes (between 82.0 - 84.0 degrees East) in decimal notation,for example
   ```
   def main():
    n = 5
    s = "sites"
    dic = {s: []}
    compositions = ["stony", "iron", "stony-iron"]
    for i in range(n):
        latitude = random.uniform(16.0, 18.0)
        longitudes = random.uniform(82.0, 84.0)
        composition = compositions[random.randint(0, 2)]
        dic[s].append({'site_id': i + 1, 'latitude': latitude, 'longitude': longitudes, 'composition': composition})
    ```
   
* calculate_trip
  * You can use this script to read in the meteorite site JSON file and calculates the time required to visit and take samples from the five sites in order.
  * Assume that Mars is a sphere (radius = 3389.5 km) and use the great-circle distance algorithm to calculate distance between points，for example
  
  
  ```
  def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    mars_radius = 3389.5
    lat1, lon1, lat2, lon2 = map(math.radians, [latitude_1, longitude_1, latitude_2, longitude_2])
    d_sigma = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1 - lon2)))
    return mars_radius * d_sigma
  ```
 
  * When the robot stops to take a sample of each meteorite, the amount of time it stops depends on the composition of the meteorite,for example
 ```
 for i in range(n):
        distance = calc_gcd(latitude, longitude, load_dict['sites'][i]['latitude'], load_dict['sites'][i]['longitude'])
        travel_time_cost = distance / speed + cost[load_dict['sites'][i]['composition']]
        sample_time_cost = cost[load_dict['sites'][i]['composition']]
        time_cost += travel_time_cost + sample_time_cost
        print(
            f'leg = {i + 1}, time to travel = {round(travel_time_cost, 2)} hr, time to sample = {round(sample_time_cost, 2)} hr')
        latitude = load_dict['sites'][i]['latitude']
        longitude = load_dict['sites'][i]['longitude']
  ```
 Sample output
 --
 ```
leg = 1, time to travel = 6.86 hr, time to sample = 3 hr
leg = 2, time to travel = 7.39 hr, time to sample = 2 hr
leg = 3, time to travel = 6.65 hr, time to sample = 1 hr
leg = 4, time to travel = 6.43 hr, time to sample = 1 hr
leg = 5, time to travel = 14.01 hr, time to sample = 3 hr
================================================
number of legs = 5, total time elapsed = 51.33 hr
```
* Stony meteorites take 1 hour to sample, from the output we can see, the lading sites of leg 3,4 are stony meteorites
* iron meteorites take 2 hours to sample, from the output we can see, the lading site of leg 2 is iron meteorites
* stony-iron meteorites take 3 hours to sample,from the output we can see, the lading sites of leg 1,5 are stony-iron meteorites

