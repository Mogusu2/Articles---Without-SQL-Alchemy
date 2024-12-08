import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

def test_article_initialization():
    author = Author("James Mogusu")
    magazine = Magazine("Tech Today", "Technology")
    article = Article(author, magazine, "Future of AI")
    assert article.title == "Future of AI"
    assert article.author == author
    assert article.magazine == magazine

def test_article_invalid_title_length():
    author = Author("James Mogusu")
    magazine = Magazine("Tech Today", "Technology")
    with pytest.raises(ValueError):
        Article(author, magazine, "AI")

def test_article_invalid_author_type():
    magazine = Magazine("Tech Today", "Technology")
    with pytest.raises(ValueError):
        Article("Invalid Author", magazine, "Future of AI")

def test_article_invalid_magazine_type():
    author = Author("James Mogusu")
    with pytest.raises(ValueError):
        Article(author, "Invalid Magazine", "Future of AI")
