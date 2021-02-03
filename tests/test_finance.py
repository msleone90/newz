from newz.finance import get_stock_data

def test_get_stock_data():
    stock_data = get_stock_data()
    assert stock_data