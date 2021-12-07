import pytest

from euclidean import euclidean, extended_euclidean


def test_euclidean():
    """
    Tests that :func:`euclidean` calculates the correct GCD.
    """
    assert 89 == euclidean(2047, 267)
    assert 1 == euclidean(47, 57)


def test_extended_euclidean():
    """
    Tests that :func:`extended_euclidean` calculates the correct modular
    inverse.
    """
    assert 17 == extended_euclidean(57, 47)


def test_bad_extended_euclidean():
    """
    Tests that :func:`extended_euclidean` raises :exc:`ValueError` when the modular
    inverse does not exist.
    """
    with pytest.raises(ValueError):
        extended_euclidean(4, 2)
