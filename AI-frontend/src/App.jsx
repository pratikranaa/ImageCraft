import React, { useState } from 'react'
import Products from './Products'
import Navbar from './Navbar';
import Forms from './Forms';

function App() {
  var [a, b] = useState(69);
  return (
  <div className="w-full h-screen bg-zinc-900 text-white">
    <Navbar /> 
    <Forms/> 
  </div> 
  )
}

export default App
