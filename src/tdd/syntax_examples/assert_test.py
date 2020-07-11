#!/usr/bin/env python
# -*- coding: utf-8 -*-

# assert_test.py

import pytest

def test_IntAssert():
	assert 1 == 1

def test_StrAssert():
	assert "str" == "str"

def test_floatAssert():
	assert 1.0 == 1.0

def test_arrayAssert():
	assert [1,2,3] == [1,2,3]

def test_dictAssert():
	assert {"1":1} == {"1":1}

from pytest import approx

# Failing Floating Point Test
def test_BadFloatCompare():
	assert (0.1 + 0.2) != 0.3

# Passing Floating Point Test
def test_GoodFloatCompare():
	val = 0.1 + 0.2
	assert val == approx(0.3)

from pytest import raises

def raisesValueException():
	raise ValueError
	# Will cause test failure:
	# pass
	

def test_Exception():
	with raises(ValueError):
		raisesValueException()