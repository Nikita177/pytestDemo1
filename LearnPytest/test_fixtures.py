import pytest


@pytest.mark.usefixtures("payload")
@pytest.mark.usefixtures("setup  ")
class TestExample2:

    def test_payload(self,payload):
        print(payload)

    def test_fix(self):
        print("Fixture")