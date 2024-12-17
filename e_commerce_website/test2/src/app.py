import os
from flask import Flask, render_template
from src.controllers.post_controller import handle_get_posts, handle_get_post, handle_create_post

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    # Handle the request to get all posts
    posts = handle_get_posts()
    # Render the template with the list of posts
    return render_template('index.html', posts=posts)

# Define the route for viewing a single post
@app.route('/post/<int:post_id>')
def post_detail(post_id):
    # Handle the request to get a specific post by ID
    post = handle_get_post(post_id)
    # Render the template with the post details
    return render_template('post_detail.html', post=post)

# Define the route for creating a new post
@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        # Handle the request to create a new post
        handle_create_post(request.form)
        # Redirect to the home page after creating a post
        return redirect(url_for('home'))
    # Render the template for the create post form
    return render_template('create_post.html')

def run_app():
    # Start the application server
    app.run(debug=True)

if __name__ == '__main__':
    run_app()