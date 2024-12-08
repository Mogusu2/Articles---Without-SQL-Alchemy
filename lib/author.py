class Author:
    def __init__(self, name):
        # Validate and set name
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name  # Use _name for the backing attribute

    @property
    def name(self):
        """Returns the name of the author. Cannot be changed."""
        return self._name

    def articles(self):
        """Returns all articles written by this author."""
        from lib.article import Article
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Returns all unique magazines this author has contributed to."""
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        """Creates a new article and associates it with this author."""
        from lib.article import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        """Returns all unique categories of magazines this author has contributed to."""
        return list(set(magazine.category for magazine in self.magazines()))
