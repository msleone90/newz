from modules import articles
import pytest

@pytest.mark.parametrize("city", [
    "Atlanta",
    "Austin",
    "Los Angeles",
    "Sarasota"
])
def test_get_articles(city):
    assert articles.get_articles(city)