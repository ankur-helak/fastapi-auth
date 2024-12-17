from flask import request, jsonify
from src.models.posts import get_all_posts, get_post_by_id, create_post

def handle_get_posts():
    """
    Handles the request to get all posts.
    """
    try:
        posts = get_all_posts()
        return jsonify(posts), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def handle_get_post(post_id):
    """
    Handles the request to get a specific post by ID.
    """
    try:
        post = get_post_by_id(post_id)
        if post:
            return jsonify(post), 200
        else:
            return jsonify({"error": "Post not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def handle_create_post():
    """
    Handles the request to create a new post.
    """
    try:
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        author = data.get('author')

        if not title or not content or not author:
            return jsonify({"error": "Missing required fields"}), 400

        new_post = create_post(title, content, author)
        return jsonify(new_post), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500