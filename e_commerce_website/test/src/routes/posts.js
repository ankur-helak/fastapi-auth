import express from 'express';
import { createPost, getPosts, getPostById, updatePost, deletePost } from '../controllers/PostController.js';

const router = express.Router();

// Route to get all posts
router.get('/posts', getPosts);

// Route to create a new post
router.post('/posts', createPost);

// Route to get a specific post by ID
router.get('/posts/:id', getPostById);

// Route to update a specific post by ID
router.put('/posts/:id', updatePost);

// Route to delete a specific post by ID
router.delete('/posts/:id', deletePost);

export default router;