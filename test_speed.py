import pytest
from speed import calculate_speed
def test_calculate_speed():
    result=calculate_speed(100, 2)
    expected=50
    
    assert result==expected

def test_calculate_speed_2():
    result=calculate_speed(150, 3)
    expected=50
    
    assert result==expected
