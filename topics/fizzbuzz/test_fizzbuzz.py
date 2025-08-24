"""
Unit tests for FizzBuzz implementation
"""
import pytest
from main import fizzbuzz


def test_fizzbuzz_basic_numbers():
    """Test that regular numbers are returned as strings"""
    result = fizzbuzz(2)
    assert result == ["1", "2"]


def test_fizzbuzz_multiples_of_3():
    """Test that multiples of 3 return 'Fizz'"""
    result = fizzbuzz(9)
    assert result[2] == "Fizz"  # 3
    assert result[5] == "Fizz"  # 6
    assert result[8] == "Fizz"  # 9


def test_fizzbuzz_multiples_of_5():
    """Test that multiples of 5 return 'Buzz'"""
    result = fizzbuzz(10)
    assert result[4] == "Buzz"   # 5
    assert result[9] == "Buzz"   # 10


def test_fizzbuzz_multiples_of_15():
    """Test that multiples of 15 return 'FizzBuzz'"""
    result = fizzbuzz(30)
    assert result[14] == "FizzBuzz"  # 15
    assert result[29] == "FizzBuzz"  # 30


def test_fizzbuzz_sequence():
    """Test the first 15 numbers of FizzBuzz sequence"""
    result = fizzbuzz(15)
    expected = [
        "1", "2", "Fizz", "4", "Buzz",
        "Fizz", "7", "8", "Fizz", "Buzz", 
        "11", "Fizz", "13", "14", "FizzBuzz"
    ]
    assert result == expected
