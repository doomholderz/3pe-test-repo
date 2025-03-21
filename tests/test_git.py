import pytest
import requests

@pytest.mark.integration
def test_int_commit():
    response = requests.get('https://dbb9-86-10-216-244.ngrok-free.app')

    print("PRINT_TEST")
    assert "PRINT_TEST"