import pytest
import requests


def test_coindesk_api():
    # Send GET request
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    # Verify response status code
    assert response.status_code == 200, "Expected status code 200"

    # Parse response JSON
    data = response.json()

    # Verify BPI currencies exist
    bpi = data.get("bpi", {})
    currencies = ["USD", "GBP", "EUR"]
    for currency in currencies:
        assert currency in bpi, f"Currency {currency} not found in response"

    # Verify GBP description
    gbp_description = bpi.get("GBP", {}).get("description")
    assert gbp_description == "British Pound Sterling", \
        f"Expected GBP description to be 'British Pound Sterling', but got '{gbp_description}'"