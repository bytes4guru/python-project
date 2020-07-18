# line_reader_test.py

            # TEST CASES: #
# - Can call read_from_file
# - read_from_file returns correct string
# - read_from_file throws exception when file doesn't exist

import pytest
from pytest import raises
from unittest.mock import MagicMock
from line_reader import read_from_file

# Note: Not utilized, as no real file is being read.
# def test_canCallReadFromFile():
# 	read_from_file("mock_file.txt")
# 	assert True

@pytest.fixture()
def mock_open(monkeypatch):
	mock_file = MagicMock()
	mock_file.readline = MagicMock(return_value = "Mock Title")
	mock_open = MagicMock(return_value = mock_file)
	monkeypatch.setattr("builtins.open", mock_open)
	return mock_open

# Note: You don't actually want to have to open a file for this test, 
# as that puts an external dependency on the test, 
# and potentially slows the test down. Hence using mocks.
def test_returnsCorrectString(mock_open, monkeypatch):
	# Update the test case to mock out the os.path.exist, 
	# and have it return true for that particular test case:
	mock_exists = MagicMock(return_value = True)
	monkeypatch.setattr("os.path.exists", mock_exists)
	result = read_from_file("mock_file.txt")
	mock_open.assert_called_once_with("mock_file.txt", "r")
	assert result == "Mock Title"

# Note: Mocking the os.path.exist functions to allow control when 
# it returns true or false depending on the test case, 
# without actually having to make modifications in the file system.
def test_throwsExceptionWithBadFile(mock_open, monkeypatch):
	mock_exists = MagicMock(return_value = False)
	monkeypatch.setattr("os.path.exists", mock_exists)
	with raises(Exception):
		result = read_from_file("mock_file.txt")