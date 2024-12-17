import mongoose from 'mongoose';

// Define the database connection string
const dbConnectionString = 'mongodb://localhost:27017/mydatabase';

// Establish the database connection
mongoose.connect(dbConnectionString, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

// Get the connection instance
const dbConnection = mongoose.connection;

// Handle connection events
dbConnection.on('error', console.error.bind(console, 'MongoDB connection error:'));
dbConnection.once('open', () => {
  console.log('Connected to the database successfully');
});

// Export the database connection instance
export { dbConnection };