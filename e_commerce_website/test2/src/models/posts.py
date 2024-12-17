from src.db import connect_to_db, close_db_connection
from src.models.post import Post
from datetime import datetime

def get_all_posts():
    """Retrieves all posts from the database."""
    connection = connect_to_db()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, title, content, author, created_at FROM posts")
        rows = cursor.fetchall()
        posts = [Post(id=row[0], title=row[1], content=row[2], author=row[3], created_at=row[4]) for row in rows]
        return posts
    finally:
        cursor.close()
        close_db_connection(connection)

def get_post_by_id(post_id):
    """Retrieves a single post by its ID."""
    connection = connect_to_db()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, title, content, author, created_at FROM posts WHERE id = %s", (post_id,))
        row = cursor.fetchone()
        if row:
            return Post(id=row[0], title=row[1], content=row[2], author=row[3], created_at=row[4])
        return None
    finally:
        cursor.close()
        close_db_connection(connection)

def create_post(title, content, author):
    """Creates a new post in the database."""
    connection = connect_to_db()
    cursor = connection.cursor()
    try:
        created_at = datetime.now()
        cursor.execute(
            "INSERT INTO posts (title, content, author, created_at) VALUES (%s, %s, %s, %s) RETURNING id",
            (title, content, author, created_at)
        )
        post_id = cursor.fetchone()[0]
        connection.commit()
        return Post(id=post_id, title=title, content=content, author=author, created_at=created_at)
    finally:
        cursor.close()
        close_db_connection(connection)