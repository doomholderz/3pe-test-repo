import pytest

@pytest.mark.integration
def test_int_commit():
    print("PRINT_TEST")
    assert "PRINT_TEST"