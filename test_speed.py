# test_calculate_speed.py
import pytest
from calculate_speed import calculate_speed

def test_calculate_speed_normal():
    result = calculate_speed(100, 5)
    assert result == 20

def test_calculate_speed_zero_time():
    result = calculate_speed(50, 0)
    assert result == "Time cannot be zero"
