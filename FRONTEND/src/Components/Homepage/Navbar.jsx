import React from 'react'

const Navbar = () => {
  return (
    <div className='relative'>
      <div className='flex justify-between pt-1'>
        <div>

        <h1>HAKIKISHA</h1>

        </div>
        <div>
          <ul className='flex gap-4 me-2'>
            <li>Home</li>
              <li>About</li>
              <li>Contact Us</li>
              <li className='bg-customh text-white px-2 rounded'>Login</li>
          </ul>
        </div>

      </div>

    </div>
    
  )
}

export default Navbar