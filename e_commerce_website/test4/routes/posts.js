const express = require('express');
const postController = require('../controllers/postController');

const router = express.Router();

// Set up a GET route to retrieve all posts using the getAllPosts function from postController
router.get('/', postController.getAllPosts);

// Set up a POST route to create a new post using the createPost function from postController
router.post('/', postController.createPost);

// Export the router for integration into the main application
module.exports = router;