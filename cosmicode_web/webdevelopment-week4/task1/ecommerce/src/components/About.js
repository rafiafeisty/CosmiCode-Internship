import React from 'react';
import './Style.css';

const About = () => {
  return (
    <>
    <div className="main">
      <div className="About">
        <h1>About Us</h1>
        <p>Welcome to our e-commerce platform! We've designed this website with simplicity and user-friendliness in mind, aiming to provide you with a seamless shopping experience. Our core functionality allows you to easily browse a wide range of products, select your desired items, and add them to your shopping cart with just a few clicks.</p>
        <p>Once you've added items to your cart, you can conveniently view all your selected products in one place. We also understand that plans change, so we've included a straightforward feature to remove any item from your cart if you decide it's not quite right. We're constantly working to enhance your journey with us.</p>
        
        <h2>Our Key Features</h2>
        <ul>
          <li><strong>Interactive User UI/UX:</strong> We prioritize a smooth, intuitive interface that makes navigating our site a breeze.</li>
          <li><strong>Simple & Structured:</strong> Our clean design ensures you can find what you're looking for without any hassle.</li>
          <li><strong>Secure Shopping:</strong> Your privacy and security are paramount. We use robust measures to protect your data and transactions.</li>
          <li><strong>Wide Product Selection:</strong> Discover a diverse range of high-quality products to meet your needs and preferences.</li>
          <li><strong>Responsive Design:</strong> Enjoy a consistent and optimal viewing experience across all your devices, whether you're on a desktop, tablet, or smartphone.</li>
        </ul>

        <h2>Our Mission</h2>
        <p>Our mission is to empower our customers by providing an accessible, reliable, and enjoyable online shopping destination. We are committed to offering quality products, exceptional customer service, and an ever-improving platform that adapts to your evolving needs.</p>
      </div>
      <div className="about-design">
          <div className="design-circle"></div>
          <div className="design-square"></div>
          <div className="design-triangle"></div>
          <div className="design-dots"></div>
        </div>
        </div>
    </>
  );
}

export default About;