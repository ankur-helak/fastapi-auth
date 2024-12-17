import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import ProductList from './ProductList';
import ProductDetail from './ProductDetail';
import Cart from './Cart';
import Checkout from './Checkout';
import Recommendations from './Recommendations';
import Auth from './Auth';
import { AuthProvider } from '../context/AuthContext';

// Main App component that sets up routing and renders other components
function App() {
  return (
    <AuthProvider>
      <Router>
        <div id="root">
          <Switch>
            <Route path="/" exact component={ProductList} />
            <Route path="/product/:id" component={ProductDetail} />
            <Route path="/cart" component={Cart} />
            <Route path="/checkout" component={Checkout} />
            <Route path="/recommendations" component={Recommendations} />
            <Route path="/auth" component={Auth} />
          </Switch>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;