import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white text-center p-3 h-10 w-full mt-auto">
      <p>© {new Date().getFullYear()} Pratik Rana. All rights reserved.</p>
    </footer>
  );
};

export default Footer;