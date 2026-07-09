import pytest

from rest_framework.test import APIClient

@pytest.fixture
def client():
    # fixture function for the custom client
    return APIClient()