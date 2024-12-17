const express = require('express');
const { getAllPosts, createPost } = require('../controllers/postController');

const router = express.Router();

// Route for getting all posts
router.get('/', (req, res) => {
    console.log('Route for getting all posts');
    getAllPosts(req, res);
});

// Route for creating a post
router.post('/', (req, res) => {
    console.log('Route for creating a post');
    createPost(req, res);
});

module.exports = router;