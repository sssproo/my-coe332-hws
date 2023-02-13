The World Has Turned and Left Me Turbid
=

* This project is for COE332 homework 03.

* This purpose of this project is imagining your robot has finished collecting its five meteorite samples and has taken them back to the Mars lab for analysis.
* You must check the latest water quality data to assess whether it is safe to analyze samples, or if the Mars lab should go on a boil water notice.

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
Access the data set
--

* Examine the water quality data set from this link https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json
* A sample of the data looks like:

```
{
  "turbidity_data": [
    {
      "datetime": "2023-02-01 00:00",
      "sample_volume": 1.19,
      "calibration_constant": 1.022,
      "detector_current": 1.137,
      "analyzed_by": "C. Milligan"
    },
    {
      "datetime": "2023-02-01 01:00",
      "sample_volume": 1.15,
      "calibration_constant": 0.975,
      "detector_current": 1.141,
      "analyzed_by": "C. Milligan"
    },
    ... etc

```

Running the Code
--

This folder has two scripts:

* part2
   * You can use this script to read in the water quality data set, and prints three key pieces of information to screen: 
    (1) the current water turbidity (taken as the average of the most recent five data points),
    (2) whether that turbidity is below a safe threshold, and 
    (3) the minimum time required for turbidity to fall below the safe threshold (if it is already below the safe threshold, the script would report “0           hours” or similar).
   * A function to calculate turbidity, for example
   ```
   def calculate_turbidity(water_data: dict):
    """This method returns turbidity

    :param water_data: water data
    :return: water turbidity
    """
    index = len(water_data['turbidity_data']) - 1
    cnt = 5
    turbidity = 0
    while cnt > 0:
        turbidity += water_data['turbidity_data'][index]['calibration_constant'] * water_data['turbidity_data'][index][
            'detector_current']
        cnt -= 1
        index -= 1
    return round(turbidity / 5, 4)
    ```
    * A function to calculate minimum time to fall below threshold turbidity, for example
    
    ```
    def calculate_minimum_time(turbidity: float):
    """This method returns minimum time to fall below threshold turbidity

    :param turbidity: current turbidity
    :return: minimum time to fall below threshold turbidity
    """
    if turbidity < 1:
        return 0.0
    return round(math.log(1 / turbidity) / math.log(1 - 0.02), 4)
    ```
   
* part3
  * You can use this script to write unit tests to test your functions described above, for example
  ```
  def test_calculate_minimum_time():
    expected_value = 8.9916
    assert round(calculate_minimum_time(1.1992), 4) == expected_value
    assert type(calculate_minimum_time(1.1992)) == float
    assert calculate_minimum_time(0) == 0.0
    assert type(calculate_minimum_time(0)) == float
    assert calculate_minimum_time(1) == 0
    assert type(calculate_minimum_time(1)) == float
    assert calculate_minimum_time(0.58) == 0
    assert type(calculate_minimum_time(0.58)) == float
  
  ```
  
 Sample output
 --
 * Turbidity is above the safe threshold
 ```
Average turbidity based on most recent five measurements = 1.1559 NTU
Warning: Turbidity is above threshold for safe use
Minimum time required to return below a safe threshold = 7.1713 hours
```


