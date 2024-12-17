const express = require('express');
const connectDB = require('./config/db');
const postRoutes = require('./routes/posts');

const app = express();

// Connect to the database
console.log('Connecting to database');
connectDB();

// Middleware to parse JSON
app.use(express.json());

// Use post routes
app.use('/api/posts', postRoutes);

// Define the port
const PORT = process.env.PORT || 5000;

// Start the server
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));