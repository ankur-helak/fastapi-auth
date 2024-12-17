// Import the Post model to interact with the database
const Post = require('../models/Post');

// Function to get all posts from the database
const getAllPosts = async (req, res) => {
    try {
        // Retrieve all posts using the Post model
        const posts = await Post.find();
        // Send the retrieved posts as a JSON response
        res.json(posts);
    } catch (error) {
        // Handle any errors by sending a 500 status and error message
        res.status(500).json({ message: 'Server Error', error: error.message });
    }
};

// Function to create a new post in the database
const createPost = async (req, res) => {
    try {
        // Extract title and content from the request body
        const { title, content } = req.body;
        
        // Create a new Post instance with the provided data
        const newPost = new Post({
            title,
            content,
            date: new Date() // Set the current date
        });

        // Save the new post to the database
        await newPost.save();

        // Send a success response with the created post
        res.status(201).json(newPost);
    } catch (error) {
        // Handle any errors by sending a 400 status and error message
        res.status(400).json({ message: 'Error creating post', error: error.message });
    }
};

// Export the controller functions for use in routes
module.exports = {
    getAllPosts,
    createPost
};