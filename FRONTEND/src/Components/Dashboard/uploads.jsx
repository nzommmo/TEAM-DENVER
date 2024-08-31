import React, { useState } from 'react';
import axios from 'axios';

const Upload = () => {
  const [bank, setBank] = useState('');
  const [statementType, setStatementType] = useState('original');
  const [file, setFile] = useState(null);
  const [responseMessage, setResponseMessage] = useState('');

  const banks = ['Chase', 'Bank of America', 'Wells Fargo']; // Update with actual bank names

  const handleGenerate = async () => {
    try {
      const response = await axios.post('/generate', {
        bank,
        statement_type: statementType,
      }, {
        responseType: 'blob' // Ensure the response type is blob for PDFs
      });

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `${bank.replace(' ', '_')}_${statementType}_statement.pdf`);
      document.body.appendChild(link);
      link.click();
    } catch (error) {
      setResponseMessage('Error generating statement');
    }
  };

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleVerify = async () => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('bank', bank);

    try {
      const response = await axios.post('/verify', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        }
      });

      setResponseMessage(response.data);
    } catch (error) {
      setResponseMessage('Error verifying statement');
    }
  };

  return (
    <div className="container">
      <h1>Bank Statement Generator and Verifier</h1>
      <form onSubmit={(e) => { e.preventDefault(); handleGenerate(); }}>
        <label htmlFor="bank">Select Bank:</label>
        <select name="bank" id="bank" value={bank} onChange={(e) => setBank(e.target.value)} required>
          <option value="">Select a bank</option>
          {banks.map((b) => (
            <option key={b} value={b}>{b}</option>
          ))}
        </select>

        <label htmlFor="statement_type">Statement Type:</label>
        <select name="statement_type" id="statement_type" value={statementType} onChange={(e) => setStatementType(e.target.value)} required>
          <option value="original">Original</option>
          <option value="fake">Fake</option>
        </select>

        <button type="submit">Generate Statement</button>
      </form>

      <form onSubmit={(e) => { e.preventDefault(); handleVerify(); }}>
        <label htmlFor="file">Upload PDF for Verification:</label>
        <input type="file" id="file" onChange={handleFileChange} required />

        <button type="submit">Verify Statement</button>
      </form>

      {responseMessage && <p>{responseMessage}</p>}
    </div>
  );
};

export default Upload;
