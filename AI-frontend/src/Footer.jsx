import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-gray-800 text-white text-center p-3 h-10 w-full mt-auto fixed bottom-0">
      <p>© {new Date().getFullYear()} <a href='https://linktr.ee/pratikrana' >Pratik Rana</a>. All rights reserved.</p>
    </footer>
  );
};

export default Footer;