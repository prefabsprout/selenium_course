import pytest


@pytest.fixture()
def user_credentials():
    return {"username": "Roman",
            "password": "Jdi1234",
            "full_username": "ROMAN IOVLEV"}
