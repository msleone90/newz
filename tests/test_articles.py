import newz.articles as article
import pytest

@pytest.mark.parametrize("city", [
    "Atlanta",
    "Austin",
    "Los Angeles",
    "Charlotte"
])
def test_get_articles(city):
    assert article.get_articles(city)