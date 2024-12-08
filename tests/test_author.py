import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

def test_author_initialization():
    author = Author("James Mogusu")
    assert author.name == "James Mogusu"

def test_author_articles():
    author = Author("James Mogusu")
    magazine = Magazine("Tech Today", "Technology")
    Article(author, magazine, "Future of AI")
    assert len(author.articles()) == 1

def test_author_magazines():
    author = Author("James Mogusu")
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")
    Article(author, magazine1, "Future of AI")
    Article(author, magazine2, "Healthy Living")
    assert len(author.magazines()) == 2

def test_author_topic_areas():
    author = Author("James Mogusu")
    magazine1 = Magazine("Tech Today", "Technology")
    magazine2 = Magazine("Health Weekly", "Health")
    Article(author, magazine1, "Future of AI")
    Article(author, magazine2, "Healthy Living")
    assert set(author.topic_areas()) == {"Technology", "Health"}
