import React from 'react'
import { PhoneCall,Mail} from 'lucide-react'
import { Facebook,Twitter,Instagram } from 'lucide-react'

const Footer = () => {
  return (
    <div className='relative mt-10'>
        <div className='flex md:flex-row sm:flex-col flex-wrap gap-10 ms-5 me-5  md:items-center justify-between  '>
            <div className='flex flex-col gap-5 flex-wrap'>
                <div>
                    <img src="" alt="logo" />
                    <h1 className=" text-lg font-semibold text-customq flex gap-1 md:text-3xl">
             HAKIKISHA
            </h1>                </div>
                <div>
                    <h1 className='text-customm text-xl'>About Us</h1>
                    <p>
                        We help you mitigate fraud.
                    </p>
                </div>
                <div>
                <h1 className='text-customm text-xl pb-3'>Contact Us</h1>
                <ul className='flex flex-col gap-3'>
                    <li className='flex gap-4'><PhoneCall size={20} className='text-customm'/> +254757876614  </li>
                    <li className='flex gap-4'><Mail size={20} className='text-customm'/> HAKIKISHA.com  </li>

                    <li></li>
                </ul>
                </div>
            </div>

            <div className='clex flex-col gap-2'>
                <div>
                <h1 className='text-customm text-xl '>Information</h1>
                </div>
                <div>
                    <ul className='flex flex-col gap-2'>
                        <li className=''>About Us</li>
                        <li>Blog</li>
                        <li>Testimonials</li>
                        <li>FAQs</li>
                        <li>Events</li>

                    </ul>

                </div>

                
            </div>
            <div>
            <h1 className='text-customm text-xl pb-3'>Helpful Links</h1>
          <ul className='flex flex-col gap-2'>
            <li >Services</li>
            <li>Supports</li>
            <li>Terms & Conditions</li>
            <li>Privacy Policy</li>

          </ul>

            </div>
            <div className='flex flex-col gap-3'>
                <div>
                    <h1 className='text-lg mb-4'>Subsribe To Our Newsletter For More Info</h1>
                </div>
                <input type="text" className='md:py-3 sm:py-2 h-[40px] px-2 rounded '  placeholder='Enter your Email'/>
               <div>
               <button className='float-left bg-customg px-3 py-1 rounded mt-2'>Subscribe</button>

               </div>
                
            </div>

        </div>
        
        <div className='mb-5'>
            <hr className='ms-5 me-5 mt-3 mb-5 ' />
            <div className='flex items-center justify-center '>
                <ul className='flex gap-3'>
                    <li className='bg-customm rounded-full p-1'><Facebook size={20}/></li>
                    <li className='bg-customm rounded-full p-1'><Twitter size={20}/></li>
                    <li className='bg-customm rounded-full p-1'><Instagram size={20}/></li>

                </ul>

            </div>
        </div>

    </div>
  )
}

export default Footer