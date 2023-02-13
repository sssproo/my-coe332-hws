import requests
import json
import math


def main():
    url = 'https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'}
    requests.get(url, headers=headers)
    water_data = json.loads(requests.get(url).text)
    turbidity = calculate_turbidity(water_data)
    hour = calculate_minimum_time(turbidity)
    print(f'Average turbidity based on most recent five measurements = {turbidity} NTU')
    if turbidity > 1:
        print('Warning: Turbidity is above threshold for safe use')
        print(f'Minimum time required to return below a safe threshold = {hour} hours')
    else:
        print('Info: Turbidity is below threshold for safe use')
        print('Minimum time required to return below a safe threshold = 0 hours')


def calculate_minimum_time(turbidity: float):
    """This method returns minimum time to fall below threshold turbidity

    :param turbidity: current turbidity
    :return: minimum time to fall below threshold turbidity
    """
    if turbidity < 1:
        return 0.0
    return round(math.log(1 / turbidity) / math.log(1 - 0.02), 4)


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


if __name__ == '__main__':
    main()
