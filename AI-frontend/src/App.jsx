import React, { useState } from 'react'
import Navbar from './Navbar';
import Forms from './Forms';
import Footer from './Footer';



function App() {
  return (
  <div className="flex flex-col min-h-screen bg-gray-800">
    <Navbar />
    <Forms/> 
    <Footer/>
  </div> 
  )
}

export default App
