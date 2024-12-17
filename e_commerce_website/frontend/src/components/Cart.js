import React, { useState, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';

/**
 * Cart component to manage and display the shopping cart.
 * 
 * This component maintains a list of items in the cart and provides a checkout functionality.
 * It uses React's useState to manage the cart items and useContext to access the user's authentication status.
 * 
 * @component
 * 
 * @returns {JSX.Element} A React component that displays the cart items and a checkout button.
 * 
 * @throws Will alert the user if they attempt to checkout without being logged in.
 */
const Cart = () => {
  // State to hold cart items
  const [cartItems, setCartItems] = useState([]);
  
  // Access user authentication context
  const { user } = useContext(AuthContext);

  /**
   * Function to handle the checkout process.
   * 
   * Checks if the user is logged in before proceeding with the checkout.
   * If the user is not logged in, an alert is shown.
   * Otherwise, it logs the cart items to the console.
   */
  const handleCheckout = () => {
    if (!user) {
      alert('Please log in to proceed with checkout.');
      return;
    }
    // Logic for handling checkout will be implemented here
    console.log('Proceeding to checkout with items:', cartItems);
  };

  return (
    <div id="cart">
      <h2>Your Shopping Cart</h2>
      {cartItems.length === 0 ? (
        <p>Your cart is empty</p>
      ) : (
        <ul>
          {cartItems.map((item, index) => (
            <li key={index}>{item.name} - ${item.price}</li>
          ))}
        </ul>
      )}
      <button id="checkout-button" onClick={handleCheckout}>
        Checkout
      </button>
    </div>
  );
};

export default Cart;
