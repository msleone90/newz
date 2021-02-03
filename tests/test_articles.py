import newz.articles as article

def test_get_articles():
    city = 'Atlanta'
    result = article.get_articles(city)
    assert result != ''