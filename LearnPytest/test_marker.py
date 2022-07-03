import pytest


@pytest.mark.smoke
def test_m1():
    print("Marker for smomke")
    assert True


@pytest.mark.skip
def test_m2():
    print("Skip")