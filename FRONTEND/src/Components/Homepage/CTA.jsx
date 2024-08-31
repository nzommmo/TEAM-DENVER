import React from 'react'
import {useNavigate } from 'react-router-dom';


const CTA = () => {
    const handleClick = () => {
        window.location.href = 'http://127.0.0.1:5000/';      };
  return (
    <div className='relative py-5'>
        <div className='mt-10 flex items-center justify-center'>
            <div className='rounded bg-customc w-2/3'>
                <div className='flex justify-between py-5 px-5'>
                    <div>
                    <h1 className='text-5xl text-customh'>Authenticate With Us <br/> <span className='text-customa'>Today</span></h1>
                    <p className='text-xl pt-5 text-customg'>A step away from Fraud</p>

                    </div>
                
                </div>
                
                <div className='flex items-center justify-end px-4 py-2'>
                <button  onClick={handleClick}   className='bg-custome text-customf px-5 py-2 rounded '>Get Started</button>
                </div>
            </div>


        </div>

    </div>
  )
}

export default CTA