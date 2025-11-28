import pytest
from speed import calculate_speed

def test_speed_calculation():
    distance = 100
    time = 5
    expected_speed = 20

    result = calculate_speed(distance, time)
    assert result == expected_speed
