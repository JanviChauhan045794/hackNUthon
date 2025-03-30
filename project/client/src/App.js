import React from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Features from './components/Features';
import Footer from './components/Footer';
import Signup from './components/Signup';
import Login from './components/Login';
import './App.css';

// Wrapper component to handle layout
const Layout = ({ children }) => {
  const location = useLocation();
  const isAuthPage = location.pathname === '/signup' || location.pathname === '/login';

  return (
    <div className="App">
      {!isAuthPage && <Navbar />}
      {children}
      {!isAuthPage && <Footer />}
    </div>
  );
};

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          <Route path="/" element={
            <>
              <Hero />
              <Features />
            </>
          } />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
