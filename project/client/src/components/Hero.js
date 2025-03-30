import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Hero.css';

const Hero = () => {
  const navigate = useNavigate();

  return (
    <div className="hero-container">
      <div className="hero-content">
        <div className="hero-text">
          <h1 className="hero-title">
            Welcome to <span className="highlight">Ayush</span>
            <span className="animate-wave">👋</span>
          </h1>
          <p className="hero-subtitle">
            Transforming ideas into digital reality with innovative solutions
          </p>
          <div className="hero-buttons">
            <button 
              className="primary-btn get-started-button" 
              onClick={() => navigate('/signup')}
            >
              Get Started
            </button>
            <button className="secondary-btn">Learn More</button>
          </div>
        </div>

        <div className="hero-image">
          <div className="animated-shape shape-1"></div>
          <div className="animated-shape shape-2"></div>
          <div className="animated-shape shape-3"></div>
          <img 
            src="/hero-illustration.svg" 
            alt="Hero Illustration"
            className="main-image"
          />
        </div>
      </div>

      <div className="hero-stats">
        <div className="stat-item">
          <span className="stat-number">500+</span>
          <span className="stat-label">Happy Clients</span>
        </div>
        <div className="stat-item">
          <span className="stat-number">1000+</span>
          <span className="stat-label">Projects</span>
        </div>
        <div className="stat-item">
          <span className="stat-number">24/7</span>
          <span className="stat-label">Support</span>
        </div>
      </div>
    </div>
  );
};

export default Hero; 