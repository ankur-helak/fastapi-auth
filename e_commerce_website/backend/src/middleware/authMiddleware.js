const jwt = require('jsonwebtoken');
const User = require('../models/User');

// Middleware function to authenticate user
const authenticateUser = (req, res, next) => {
    // Get token from request headers
    const token = req.header('Authorization');

    // Check if token is not present
    if (!token) {
        return res.status(401).json({ message: 'No token, authorization denied' });
    }

    try {
        // Verify token
        const decoded = jwt.verify(token, process.env.JWT_SECRET);

        // Attach user from the payload to the request object
        req.user = decoded.user;

        // Proceed to the next middleware or route handler
        next();
    } catch (err) {
        // If token is invalid, respond with an error
        res.status(401).json({ message: 'Token is not valid' });
    }
};

module.exports = authenticateUser;
