"""This file tests the helper_function.py module"""

import helper_function as hf

# Add 3 basic pytests to helper_function
def test_say_hello():
    """Test the say_hello function in helper_function.py"""
    assert hf.say_hello() == 'hello'

def test_random_bowling_score():
    """Test the random_bowling_score function in helper_function.py"""
    assert hf.random_bowling_score() >= 1
    assert hf.random_bowling_score() <= 300

def test_random_float():
    """Test the random_float function in helper_function.py"""
    min_val = 3
    max_val = 4000
    assert hf.random_float(min_val, max_val) >= min_val
    assert hf.random_float(min_val, max_val) < max_val
