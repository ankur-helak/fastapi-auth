const Post = require('../models/Post');

// Function to get all posts
exports.getAllPosts = async (req, res) => {
    try {
        console.log('Fetching all posts');
        const posts = await Post.find(); // Retrieve all posts from the database
        res.json(posts); // Send the posts as a JSON response
    } catch (err) {
        console.error('Server Error', err);
        res.status(500).send('Server Error'); // Send a server error message if something goes wrong
    }
};

// Function to create a new post
exports.createPost = async (req, res) => {
    try {
        console.log('Creating a new post');
        const { title, content } = req.body; // Destructure title and content from the request body
        const newPost = new Post({
            title,
            content,
            date: new Date() // Set the current date for the post
        });

        const post = await newPost.save(); // Save the new post to the database
        res.json(post); // Send the created post as a JSON response
    } catch (err) {
        console.error('Server Error', err);
        res.status(500).send('Server Error'); // Send a server error message if something goes wrong
    }
};