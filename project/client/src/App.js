import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import Footer from './components/Footer';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Hero />
        <main className="main-content">
          {/* Your routes and other content will go here */}
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
