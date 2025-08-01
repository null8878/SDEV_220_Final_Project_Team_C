import os
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils import compute_balances


def test_compute_balances_basic():
    roommates = ['Alice', 'Bob', 'Carol', 'Dave']
    expenses = [
        {'amount': 100},
        {'amount': 50},
    ]
    result = compute_balances(roommates, expenses)
    expected = {
        'Bob owes Alice': 37.5,
        'Carol owes Alice': 37.5,
        'Dave owes Alice': 37.5,
    }
    assert result == expected


def test_compute_balances_empty_roommates():
    assert compute_balances([], []) == {}
