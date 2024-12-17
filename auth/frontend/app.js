// Function to fetch products from the backend API and update the DOM
async function fetchProducts() {
    try {
        const response = await fetch('/api/products'); // Fetch products from the backend API
        const products = await response.json(); // Parse the JSON response
        const productList = document.getElementById('product-list'); // Get the product list DOM element

        // Clear the existing product list
        productList.innerHTML = '';

        // Iterate over the products and create HTML elements for each
        products.forEach(product => {
            const productItem = document.createElement('div');
            productItem.className = 'product-item';
            productItem.innerHTML = `
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <p>Price: $${product.price}</p>
                <button onclick="addToCart(${product.id})">Add to Cart</button>
            `;
            productList.appendChild(productItem); // Append the product item to the product list
        });
    } catch (error) {
        console.error('Error fetching products:', error); // Log any errors
    }
}

// Function to add a product to the shopping cart
function addToCart(productId) {
    const cart = document.getElementById('cart'); // Get the cart DOM element
    const cartItem = document.createElement('div');
    cartItem.className = 'cart-item';
    cartItem.innerHTML = `Product ID: ${productId}`;
    cart.appendChild(cartItem); // Append the cart item to the cart
}

// Function to handle the checkout process
function checkout() {
    const cart = document.getElementById('cart'); // Get the cart DOM element
    const checkoutButton = document.getElementById('checkout-button'); // Get the checkout button DOM element

    // Add event listener to the checkout button
    checkoutButton.addEventListener('click', () => {
        alert('Checkout process initiated!'); // Alert the user that checkout has started
        cart.innerHTML = ''; // Clear the cart after checkout
    });
}

// Initialize the app by fetching products and setting up event listeners
document.addEventListener('DOMContentLoaded', () => {
    fetchProducts(); // Fetch products when the DOM is fully loaded
    checkout(); // Set up the checkout process
});