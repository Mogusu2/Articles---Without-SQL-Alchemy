import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

def test_magazine_initialization():
    magazine = Magazine("Tech Today", "Technology")
    assert magazine.name == "Tech Today"
    assert magazine.category == "Technology"

def test_magazine_articles():
    author = Author("James Mogusu")
    magazine = Magazine("Tech Today", "Technology")
    Article(author, magazine, "Future of AI")
    assert len(magazine.articles()) == 1

def test_magazine_contributors():
    author1 = Author("James Mogusu")
    author2 = Author("Juicy Jan")
    magazine = Magazine("Tech Today", "Technology")
    Article(author1, magazine, "Future of AI")
    Article(author2, magazine, "Tech Revolution")
    assert len(magazine.contributors()) == 2

def test_magazine_article_titles():
    author = Author("James Mogusu")
    magazine = Magazine("Tech Today", "Technology")
    Article(author, magazine, "Future of AI")
    Article(author, magazine, "Tech Revolution")
    assert magazine.article_titles() == ["Future of AI", "Tech Revolution"]

def test_magazine_contributing_authors():
    author = Author("James Mogusu")
    magazine = Magazine("Tech Today", "Technology")
    Article(author, magazine, "Future of AI")
    Article(author, magazine, "Tech Revolution")
    Article(author, magazine, "AI and Ethics")
    assert magazine.contributing_authors() == [author]
