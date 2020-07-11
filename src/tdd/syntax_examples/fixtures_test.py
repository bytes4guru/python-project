#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fixtures_test.py

import pytest

@pytest.fixture()
def setup1():
    print("\nSetup 1!")

# Argument Example
def test1(setup1):
    print("Executing test1!")
    assert True

# Decorator Example
@pytest.mark.usefixtures("setup1")
def test2():
    print("Executing test2!")
    assert True

# autouse Example
@pytest.fixture(autouse=True)
def setup2():
    print("\nSetup!")

def test3():
    print("Executing test3!")
    assert True

def test4():
    print("Executing test4!")
    assert True

# Yield Example
@pytest.fixture()
def setup3():
    print("\nSetup 3!")
    yield
    print("\nTeardown 3!")

# Addfinalizer Example
@pytest.fixture()
def setup4(request):
    print("\nSetup 4!")

    def teardown_a():
        print("\nTeardown A!")

    def teardown_b():
        print("\nTeardown B!")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test5(setup3):
    print("Executing test5!")
    assert True

def test6(setup4):
    print("Executing test6!")
    assert True

# Scope Example
@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("\nSetup Session!")

@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("\nSetup Module!")

@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup Function!")

class TestClass:
    def test7(self):
        print("Executing test7!")
        assert True

    def test8(self):
        print("Executing test8!")
        assert True