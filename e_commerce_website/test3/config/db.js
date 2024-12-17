const mongoose = require('mongoose');

// Function to connect to MongoDB
const connectDB = async () => {
  try {
    // Connect to MongoDB using the URI from environment variables
    await mongoose.connect(process.env.MONGO_URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    console.log('MongoDB connected'); // Message indicating successful connection
  } catch (err) {
    console.error('Server Error', err.message); // Message indicating server error
    process.exit(1); // Exit process with failure
  }
};

// Export the connectDB function for use in other parts of the application
module.exports = connectDB;