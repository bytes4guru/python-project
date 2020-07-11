#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fizz_buzz_test.py

import pytest

# FIZZBUZZ #
def fizz_buzz (value):
    if fizz_buzz_multiple(value, 3):
        if fizz_buzz_multiple(value, 5):
            return "FizzBuzz!"
        return "Fizz"
    if fizz_buzz_multiple(value, 5):
        return "Buzz"
    return str(value)

def fizz_buzz_multiple(value, mod):
    return ( value % mod == 0)

# TESTS #
def test_canAssertTrue():
    assert True

# Redundant, as the following test case
# demonstrates that fizz_buzz can be called.
def test_canFizzBuzzBeCalled():
    fizz_buzz(1)

def test_returns1With1PassedIn():
    return_value = fizz_buzz(1)
    assert return_value == "1"

def test_returns2With2PassedIn():
    return_value = fizz_buzz(2)
    assert return_value == "2"

# Above two tests can be refactored as follows:
def check_fizz_buzz(value, expected_return_value):
    return_value = fizz_buzz(value)
    assert return_value == expected_return_value

def test_returns1With1PassedIn():
    check_fizz_buzz(1, "1")

def test_returns2With2PassedIn():
    check_fizz_buzz(2, "2")

def test_returnsFizzWith3PassedIn():
    check_fizz_buzz(3, "Fizz")

def test_returnsBuzzWith5PassedIn():
    check_fizz_buzz(5, "Buzz")

def test_returnsFizzWith6PassedIn():
    check_fizz_buzz(6, "Fizz")

def test_returnsBuzzWith10PassedIn():
    check_fizz_buzz(10, "Buzz")

def test_returnsFizzBuzzWith15PassedIn():
    check_fizz_buzz(15, "FizzBuzz!")