# Simple Unit Test Example

import pytest

# Product Code
def string_length( theString ):
    return len(theString)

# A Unit Test
def test_string_length():
    # 1. The Setup
    testString = "1"
    # 2. The Action 
    result = string_length(testString)
    # 3. The Assertion
    assert result == 1