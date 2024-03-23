import React, { useState } from 'react'

function Products({naam}) {
  const [a, b] = useState(false);
  return (
    <div className='h-60 w-full bg-zinc-600'>
      <h1 className={`${a === false ? "text-red-600" : "text-green-600" }`}>{a === false ? "hello" : "Goodbye"}</h1>
      <button className='px-3 y-1 bg-red-500 rounded-md text-s' onClick={() => b(!a)}>Toggle</button>
    </div>
  )
}

export default Products
