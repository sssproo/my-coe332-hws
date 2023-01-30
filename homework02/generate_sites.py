import random
import json


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
    with open("sites.json", 'w') as write_f:
        json.dump(dic, write_f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
