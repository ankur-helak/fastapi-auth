import React, { useEffect, useState } from 'react';
import { fetchProducts } from '../utils/api';

// Recommendations component to display product recommendations
const Recommendations = () => {
  // State to hold recommended products
  const [recommendedProducts, setRecommendedProducts] = useState([]);

  // Fetch recommended products when the component mounts
  useEffect(() => {
    const getRecommendedProducts = async () => {
      try {
        // Fetch products from the API
        const products = await fetchProducts();
        // For simplicity, let's assume the first 5 products are recommendations
        setRecommendedProducts(products.slice(0, 5));
      } catch (error) {
        console.error('Error fetching recommended products:', error);
      }
    };

    getRecommendedProducts();
  }, []);

  return (
    <div id="recommendations">
      <h2>Recommended Products</h2>
      <ul>
        {recommendedProducts.map((product) => (
          <li key={product.id}>
            <h3>{product.name}</h3>
            <p>{product.description}</p>
            <p>Price: ${product.price}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Recommendations;