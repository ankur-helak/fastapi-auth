import React, { useState, useEffect } from 'react';
import { fetchProductDetails } from '../utils/api';

// ProductDetail component to display detailed information about a single product
const ProductDetail = ({ productId }) => {
  // State to hold product details
  const [product, setProduct] = useState(null);
  // State to handle loading status
  const [loading, setLoading] = useState(true);
  // State to handle error status
  const [error, setError] = useState(null);

  // useEffect hook to fetch product details when component mounts or productId changes
  useEffect(() => {
    const getProductDetails = async () => {
      try {
        // Fetch product details using the utility function
        const productData = await fetchProductDetails(productId);
        // Set the product data to state
        setProduct(productData);
      } catch (err) {
        // Set error state if fetching fails
        setError(err.message);
      } finally {
        // Set loading to false after fetching is complete
        setLoading(false);
      }
    };

    getProductDetails();
  }, [productId]);

  // Function to handle adding product to cart
  const handleAddToCart = () => {
    // Logic to add product to cart
    console.log(`Product ${productId} added to cart`);
  };

  // Render loading state
  if (loading) return <div id="product-detail">Loading...</div>;

  // Render error state
  if (error) return <div id="product-detail">Error: {error}</div>;

  // Render product details
  return (
    <div id="product-detail">
      {product && (
        <>
          <h1>{product.name}</h1>
          <p>{product.description}</p>
          <p>Price: ${product.price}</p>
          <button id="add-to-cart-button" onClick={handleAddToCart}>
            Add to Cart
          </button>
        </>
      )}
    </div>
  );
};

export default ProductDetail;
