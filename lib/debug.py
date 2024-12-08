from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

# Create some authors
author1 = Author("James Mogusu")
author2 = Author("Juicy Jan")

# Create some magazines
magazine1 = Magazine("Tech Today", "Technology")
magazine2 = Magazine("Health Weekly", "Health")

# Create some articles
article1 = Article(author1, magazine1, "Future of AI")
article2 = Article(author1, magazine2, "Healthy Living Tips")
article3 = Article(author2, magazine1, "Tech Innovations")

# Debugging examples
print(author1.articles())  # [article1, article2]
print(magazine1.articles())  # [article1, article3]
print(magazine1.contributors())  # [author1, author2]
