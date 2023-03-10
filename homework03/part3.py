from part2 import calculate_turbidity, calculate_minimum_time


def test_calculate_turbidity():
    water_data = {'turbidity_data': [
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
        {
            "datetime": "2023-02-01 02:00",
            "sample_volume": 1.15,
            "calibration_constant": 1.022,
            "detector_current": 1.1300000000000001,
            "analyzed_by": "C. Milligan"
        },
        {
            "datetime": "2023-02-01 03:00",
            "sample_volume": 1.18,
            "calibration_constant": 0.989,
            "detector_current": 1.129,
            "analyzed_by": "R. Zhang"
        },
        {
            "datetime": "2023-02-01 04:00",
            "sample_volume": 1.19,
            "calibration_constant": 1.029,
            "detector_current": 1.189,
            "analyzed_by": "J. Maertz"
        }]}
    expected_value = 1.1539
    assert round(calculate_turbidity(water_data), 7) == expected_value
    assert type(calculate_turbidity(water_data)) == float
    water_data = {'turbidity_data': [{
        "datetime": "2023-02-12 16:00",
        "sample_volume": 1.2,
        "calibration_constant": 0.959,
        "detector_current": 1.167,
        "analyzed_by": "K. Judkins"
    },
        {
            "datetime": "2023-02-12 17:00",
            "sample_volume": 1.24,
            "calibration_constant": 0.997,
            "detector_current": 1.1360000000000001,
            "analyzed_by": "R. Zhang"
        },
        {
            "datetime": "2023-02-12 18:00",
            "sample_volume": 1.22,
            "calibration_constant": 1.026,
            "detector_current": 1.1380000000000001,
            "analyzed_by": "R. Zhang"
        },
        {
            "datetime": "2023-02-12 19:00",
            "sample_volume": 1.16,
            "calibration_constant": 1.031,
            "detector_current": 1.1400000000000001,
            "analyzed_by": "C. Kight"
        },
        {
            "datetime": "2023-02-12 20:00",
            "sample_volume": 1.22,
            "calibration_constant": 1.017,
            "detector_current": 1.1620000000000001,
            "analyzed_by": "C. Kight"
        },
        {
            "datetime": "2023-02-12 21:00",
            "sample_volume": 1.24,
            "calibration_constant": 0.972,
            "detector_current": 1.115,
            "analyzed_by": "A. Mendoza"
        }
    ]}
    expected_value = 1.1482
    assert round(calculate_turbidity(water_data), 7) == expected_value
    assert type(calculate_turbidity(water_data)) == float


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
