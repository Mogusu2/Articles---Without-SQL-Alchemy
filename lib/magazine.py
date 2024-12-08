class Magazine:
    all = []

    def __init__(self, name, category):
        # Validate and set name and category
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def articles(self):
        """Returns all articles published in this magazine."""
        from lib.article import Article
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Returns all unique authors who have contributed to this magazine."""
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        """Returns all article titles for this magazine."""
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        """Returns authors with more than 2 articles in this magazine."""
        from collections import Counter
        authors = Counter(article.author for article in self.articles())
        return [author for author, count in authors.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        """Returns the magazine with the most articles."""
        return max(cls.all, key=lambda magazine: len(magazine.articles()), default=None)
