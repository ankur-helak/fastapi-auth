const express = require('express');
const { getProducts, getProductById } = require('./controllers/productController');
const { registerUser, loginUser } = require('./controllers/authController');
const { processPayment } = require('./controllers/paymentController');
const { authenticateUser } = require('./middleware/authMiddleware');

const router = express.Router();

// Product Routes
router.get('/products', getProducts);
router.get('/products/:id', getProductById);

// Authentication Routes
router.post('/auth/register', registerUser);
router.post('/auth/login', loginUser);

// Payment Routes
router.post('/payments/process', authenticateUser, processPayment);

module.exports = router;