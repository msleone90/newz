from newz.newz import get_location

def test_get_location():
    geolocation = get_location()
    assert geolocation