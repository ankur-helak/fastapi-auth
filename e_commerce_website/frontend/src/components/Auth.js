import React, { useState } from 'react';
import { loginUser, registerUser } from '../utils/api'; // Importing utility functions for API calls
import { useAuth } from '../context/AuthContext'; // Importing custom hook to use authentication context

// Auth component to handle user authentication
const Auth = () => {
  const [isLogin, setIsLogin] = useState(true); // State to toggle between login and register forms
  const [email, setEmail] = useState(''); // State to store email input
  const [password, setPassword] = useState(''); // State to store password input
  const { setUser } = useAuth(); // Destructuring setUser function from AuthContext

  // Function to handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (isLogin) {
        // If login form is active, call loginUser API
        const user = await loginUser({ email, password });
        setUser(user); // Set the authenticated user in context
      } else {
        // If register form is active, call registerUser API
        const user = await registerUser({ email, password });
        setUser(user); // Set the registered user in context
      }
    } catch (error) {
      console.error('Authentication error:', error); // Log any errors
    }
  };

  return (
    <div>
      <h2>{isLogin ? 'Login' : 'Register'}</h2>
      <form id={isLogin ? 'login-form' : 'register-form'} onSubmit={handleSubmit}>
        <div>
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit">{isLogin ? 'Login' : 'Register'}</button>
      </form>
      <button onClick={() => setIsLogin(!isLogin)}>
        {isLogin ? 'Switch to Register' : 'Switch to Login'}
      </button>
    </div>
  );
};

export default Auth;