// Import necessary modules
const express = require('express');
const mongoose = require('mongoose');
const { connectDB } = require('./config/db');
const productRoutes = require('./routes').productRoutes;
const authRoutes = require('./routes').authRoutes;
const paymentRoutes = require('./routes').paymentRoutes;

// Initialize the Express application
const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// Connect to the MongoDB database
connectDB();

// Define API routes
app.use('/api/products', productRoutes);
app.use('/api/auth', authRoutes);
app.use('/api/payments', paymentRoutes);

// Define the port the server will listen on
const PORT = process.env.PORT || 5000;

// Function to start the server
function startServer() {
  app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
  });
}

// Export the startServer function
module.exports = { startServer };