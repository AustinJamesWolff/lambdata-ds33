from wallet import Wallet
import pytest


# Functions are first-class objects in Python.
# A function works like a variable and can be passed to another function

# Make a fixture to serve as an empty wallet
# Then make a fixture to serve as a wallet with $20

@pytest.fixture
def empty_wallet():
    return Wallet()

@pytest.fixture
def wallet_20():
    return Wallet(20)

# All test functions must begin with test_
def test_empty_wallet():
    """returns a wallet object with a balance of 0"""
    assert Wallet().balance == 0

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet_20):
    assert wallet_20.balance == 20