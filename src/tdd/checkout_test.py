#!/usr/bin/env python
# -*- coding: utf-8 -*-

# checkout_test.py

            # TEST CASES: #
#
# - Can create an instance of the Checkout class
# - Can add an item price
# - Can add an item
# - Can calculate the current total
# - Can add multiple items and get correct total
# - Can add discount rules
# - Can apply discount rules to the total
# - Exception is Thrown for Item Added without a Price

from checkout import Checkout
import pytest

# Instantiate the class for easy reuse:
@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("Apple", 1.25)
    checkout.addItemPrice("Carrot", 2.25)
    checkout.addItemPrice("Figs", 3.50)
    return checkout

def test_CanAddItemPrice(checkout):
    checkout.addItem("Apple")
    assert True

def test_CanCalcuateTotal(checkout):
    checkout.addItem("Carrot")
    assert checkout.calculateTotal() == 2.25

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("Apple")
    checkout.addItem("Carrot")
    assert checkout.calculateTotal() == 3.50

def test_CanAddDiscountRule(checkout):
    checkout.addItem("Figs")
    checkout.addItem("Figs")
    checkout.addItem("Figs")
    checkout.addDiscount("Figs", 3, 5.50)
    assert checkout.calculateTotal() == 5.50

def test_ExceptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addItem("Oranges")
    assert True