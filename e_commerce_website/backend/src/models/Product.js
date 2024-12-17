const mongoose = require('mongoose');

// Define the ProductSchema using Mongoose
const ProductSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        trim: true
    },
    description: {
        type: String,
        required: true,
        trim: true
    },
    price: {
        type: Number,
        required: true,
        min: 0
    },
    category: {
        type: String,
        required: true,
        trim: true
    },
    stock: {
        type: Number,
        required: true,
        min: 0
    },
    imageUrl: {
        type: String,
        required: true,
        trim: true
    }
}, {
    timestamps: true // Automatically manage createdAt and updatedAt fields
});

// Create the Product model using the ProductSchema
const Product = mongoose.model('Product', ProductSchema);

// Export the Product model
module.exports = Product;