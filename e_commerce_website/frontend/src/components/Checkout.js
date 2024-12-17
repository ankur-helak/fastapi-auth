import React, { useState } from 'react';
import { processPayment } from '../utils/api';

// Checkout component to handle the checkout process and payment gateway integration
const Checkout = () => {
  // State to manage form inputs and payment status
  const [formData, setFormData] = useState({
    name: '',
    cardNumber: '',
    expiryDate: '',
    cvv: ''
  });
  const [paymentStatus, setPaymentStatus] = useState(null);

  // Handle input changes in the form
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  // Handle form submission and process payment
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await processPayment(formData);
      setPaymentStatus(response.success ? 'Payment Successful' : 'Payment Failed');
    } catch (error) {
      setPaymentStatus('Payment Error');
    }
  };

  return (
    <div id="checkout-form">
      <h2>Checkout</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name on Card</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label htmlFor="cardNumber">Card Number</label>
          <input
            type="text"
            id="cardNumber"
            name="cardNumber"
            value={formData.cardNumber}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label htmlFor="expiryDate">Expiry Date</label>
          <input
            type="text"
            id="expiryDate"
            name="expiryDate"
            value={formData.expiryDate}
            onChange={handleInputChange}
            required
          />
        </div>
        <div>
          <label htmlFor="cvv">CVV</label>
          <input
            type="text"
            id="cvv"
            name="cvv"
            value={formData.cvv}
            onChange={handleInputChange}
            required
          />
        </div>
        <button type="submit" id="payment-button">Pay Now</button>
      </form>
      {paymentStatus && <p>{paymentStatus}</p>}
    </div>
  );
};

export default Checkout;