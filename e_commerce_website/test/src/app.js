import express from 'express';
import { dbConnection } from './db.js';
import postsRouter from './routes/posts.js';

// Initialize the express application
const app = express();

// Connect to the database
dbConnection();

// Use middleware to parse JSON requests
app.use(express.json());

// Use the posts router for handling '/posts' routes
app.use('/posts', postsRouter);

// Define the port the server will listen on
const PORT = process.env.PORT || 3000;

// Start the server and log a message indicating the server is running
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});