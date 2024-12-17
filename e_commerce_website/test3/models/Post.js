const mongoose = require('mongoose');

// Define the PostSchema with fields for title, content, and date
const PostSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    trim: true
  },
  content: {
    type: String,
    required: true
  },
  date: {
    type: Date,
    default: Date.now
  }
});

// Create the Post model using the PostSchema
const Post = mongoose.model('Post', PostSchema);

console.log('Post model created');

// Export the Post model for use in other parts of the application
module.exports = Post;