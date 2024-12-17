from datetime import datetime

class Post:
    """
    Represents a single post entity.
    """

    def __init__(self, id: int, title: str, content: str, author: str, created_at: datetime):
        """
        Initializes a new instance of the Post class.

        :param id: The unique identifier for the post.
        :param title: The title of the post.
        :param content: The content of the post.
        :param author: The author of the post.
        :param created_at: The datetime when the post was created.
        """
        self.id = id
        self.title = title
        self.content = content
        self.author = author
        self.created_at = created_at

    def __repr__(self):
        """
        Returns a string representation of the Post instance.
        """
        return f"Post(id={self.id}, title={self.title}, author={self.author}, created_at={self.created_at})"