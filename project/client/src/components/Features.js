import React from "react";
import './Features.css';

const features = [
  {
    title: "Farmer-Verified QR Traceability",
    description: "Scan to see the journey of your food - from farm soil to your plate with blockchain-backed verification",
    number: "01",
    icon: "🏷️",
    tag: "Transparency"
  },
  {
    title: "Virtual Herbal Garden Explorer",
    description: "Explore medicinal plants in 3D - rotate, zoom, and learn Ayurvedic uses before buying",
    number: "02",
    icon: "🌿",
    tag: "Interactive"
  },
  {
    title: "AYUSH-Certified Product Kits",
    description: "Pre-made wellness bundles (Immunity/Digestion/Sleep) curated by herbal experts",
    number: "03",
    icon: "🧪",
    tag: "Wellness"
  },
  {
    title: "Live Farm Stories",
    description: "Watch real-time farm updates - see your food growing via farmer-shared videos",
    number: "04",
    icon: "📹",
    tag: "Real-time"
  },
  {
    title: "Seasonal Availability Calendar",
    description: "Know what's in harvest near you - plan orders around peak freshness periods",
    number: "05",
    icon: "🗓️",
    tag: "Seasonal"
  },
  {
    title: "Community Impact Dashboard",
    description: "See how your purchase supports small farmers - carbon saved, livelihoods impacted",
    number: "06",
    icon: "📊",
    tag: "Impact"
  }
];

const Features = () => {
  return (
    <section className="features-wrapper">
      <div className="features-container">
        <div className="features-header">
          <span className="features-subtitle">Our Innovative Features</span>
          <h2 className="features-title">
            Connecting You with 
            <span className="highlight"> Nature's Best</span>
          </h2>
          <p className="features-description">
            Experience the future of Ayurvedic farming and wellness through our cutting-edge platform
          </p>
        </div>
        
        <div className="features-grid">
          {features.map((feature) => (
            <div key={feature.number} className="feature-card">
              <div className="card-header">
                <div className="icon-wrapper">
                  <div className="icon-container">
                    <span className="feature-icon">{feature.icon}</span>
                  </div>
                  <span className="feature-tag">{feature.tag}</span>
                </div>
                <span className="feature-number">{feature.number}</span>
              </div>
              <div className="card-content">
                <h3 className="card-title">{feature.title}</h3>
                <p className="card-description">{feature.description}</p>
              </div>
              <div className="card-footer">
                <div className="learn-more">
                  Explore Feature
                  <svg className="arrow-icon" viewBox="0 0 24 24">
                    <path d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z" />
                  </svg>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Features; 