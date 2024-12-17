// Import necessary modules
const { processPayment } = require('../services/paymentService');

// Controller function to handle payment processing
async function processPayment(req, res) {
    const { amount, token } = req.body;
    try {
        const charge = await stripe.charges.create({
            amount,
            currency: 'usd',
            source: token,
        });
        res.send('Payment successful');
    } catch (err) {
        console.error('Payment processing error:', err);
        res.status(500).send('Payment failed');
    }
}



// Export the controller function
module.exports = {
    processPayment
};
