import mongoose from 'mongoose';

// Define the schema for a Post
const postSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    trim: true
  },
  content: {
    type: String,
    required: true
  },
  author: {
    type: String,
    required: true
  },
  createdAt: {
    type: Date,
    default: Date.now
  }
});

// Create and export the Post model using the defined schema
const Post = mongoose.model('Post', postSchema);

export default Post;