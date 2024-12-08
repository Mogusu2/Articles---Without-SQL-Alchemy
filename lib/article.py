from lib.author import Author
from lib.magazine import Magazine

class Article:
    all = []  # Holds all created article instances

    def __init__(self, author, magazine, title):
        # Validate inputs
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)  # Adds this instance to the global list of articles

    @property
    def title(self):
        """Returns the title of the article. Cannot be changed."""
        return self._title
