import pytest
from application import Security

@pytest.fixture
def security_data():
    return {"name": 'IBM', "target_pct": 20, "current_pct": 10, "unit_price": 150, "asset_amount": 100000}

@pytest.mark.parametrize("current_pct,target_pct,expected_variance",
                         [
                             (30, 20, 67),
                             (10, 20, -66),
                             (10.5, 20, -63),
                             (100, 100, 0),
                             (0, 0, 0),
                         ])
def test_variance(security_data, current_pct, target_pct, expected_variance):
    variance = Security(**{**security_data, "current_pct": current_pct, "target_pct": target_pct}).shares_to_variance
    assert variance == expected_variance


@pytest.mark.parametrize("incorrect_data,error_pattern",
                         [
                             ({"unit_price": -1}, "unit_price"),
                             ({"target_pct": 101}, "target_pct"),
                             ({"target_pct": -1}, "target_pct"),
                             ({"current_pct": 101}, "current_pct"),
                             ({"current_pct": -1}, "current_pct"),
                         ])
def test_data_validation(security_data, incorrect_data, error_pattern):
    with pytest.raises(ValueError, match=error_pattern):
        Security(**{**security_data, **incorrect_data})
