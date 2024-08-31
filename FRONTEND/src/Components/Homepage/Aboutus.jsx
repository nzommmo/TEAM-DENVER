import React from 'react'
import { DollarSign,Receipt,Box} from 'lucide-react'

const Aboutus = () => {
  return (
    <div className='relative mt-5'>
        <div>
            <hr className='opacity-60' />
            <div className='flex items-center mt-3 justify-center'>
                <h1 className='text-xl'>Why Hakikisha</h1>
            </div>
        </div>
        <div>
            <div className='grid grid-cols-3 ms-5 gap-5 mt-3'>
                <div>
                    <h1 className='py-2 flex gap-1'><DollarSign/>Income Verification Services</h1>
                    <p> <span className='font-semibold'>Loan Approval Support:</span> Automate the verification of income statements submitted by loan applicants, ensuring the authenticity of the documents and reducing the risk of fraudulent applications.</p>
                    <p className='py-2'><span className='font-semibold '>Scholarship Eligibility Verification:</span> Verify income documents submitted for scholarship applications to ensure that only eligible candidates receive financial aid.</p>
                </div>
                <div>
                    <h1 className='py-2 flex gap-1'><Receipt/>Bank Statement Authentication</h1>
                    <p><span className='font-semibold'>Fraud Detection:</span> Analyze bank statements to detect anomalies, inconsistencies, or signs of forgery, providing institutions with reliable assessments.</p>
                    <p className='py-2'><span className='font-semibold'>Document Validation:</span> Use advanced algorithms to validate the authenticity of bank statements, ensuring that they have not been tampered with.</p>
                </div>
                <div>
                    <h1 className='py-2 flex gap-1'><Box/>Data Privacy and Security</h1>
                    <p><span className='font-semibold'>Secure Data Handling:</span> Ensure that all bank statements and financial data are handled securely, protecting the privacy of individuals and institutions.</p>
                    <p className='py-2'><span className='font-semibold'>Compliance with Data Protection Laws:</span> Adhere to global data protection regulations, ensuring that the verification process is both effective and legally compliant.</p>
                </div>
                
                
            </div>
        </div>

    </div>
  )
}

export default Aboutus