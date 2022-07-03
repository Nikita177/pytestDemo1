import pytest


@pytest.fixture
def setup():
    print("Stepup")
    yield
    print("tear")

@pytest.fixture()
def payload():
    return ["Nikita","Raikar"]