# import pytest
import lambdata as ld

def test_increment_int():
    assert ld.increment(3) == 4
    assert ld.increment(100) == 101
    assert ld.increment(-5) == -4
