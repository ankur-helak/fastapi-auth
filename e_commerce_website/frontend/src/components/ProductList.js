import React, { useEffect, useState } from 'react';
import { fetchProducts } from '../utils/api';

/**
 * ProductList component fetches and displays a list of products.
 * 
 * This component uses the `useEffect` hook to fetch product data from an API
 * when the component is mounted. The fetched products are stored in the `products`
 * state variable and are rendered as a list of `ProductItem` components.
 * 
 * @returns {JSX.Element} A React component that renders a list of products.
 * 
 * @throws Will log an error to the console if fetching products fails.
 */
const ProductList = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const loadProducts = async () => {
      try {
        const productList = await fetchProducts();
        setProducts(productList);
      } catch (error) {
        console.error('Failed to fetch products:', error);
      }
    };

    loadProducts();
  }, []);

  return (
    <div id="product-list">
      {products.map(product => (
        <ProductItem key={product.id} {...product} />
      ))}
    </div>
  );
};

/**
 * ProductItem component displays individual product details.
 * 
 * @param {Object} props - The properties object.
 * @param {number} props.id - The unique identifier for the product.
 * @param {string} props.name - The name of the product.
 * @param {string} props.description - A brief description of the product.
 * @param {number} props.price - The price of the product.
 * 
 * @returns {JSX.Element} A React component that renders product details.
 */
const ProductItem = ({ id, name, description, price }) => (
  <div id="product-item">
    <h2>{name}</h2>
    <p>{description}</p>
    <p>Price: ${price}</p>
  </div>
);

export default ProductList;
