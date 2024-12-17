// Import necessary modules and files
const express = require('express');
const connectDB = require('./config/db');
const postsRouter = require('./routes/posts');

// Initialize the Express application
const app = express();

// Connect to the database
connectDB();

// Middleware to parse JSON requests
app.use(express.json());

// Use the posts router for handling routes under /api/posts
app.use('/api/posts', postsRouter);

// Define the port to run the server on, defaulting to 5000 if not specified
const PORT = process.env.PORT || 5000;

// Start the server and listen on the specified port
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});