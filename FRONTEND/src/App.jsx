import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Components/Homepage/Home';
import Dashboard from './Components/Dashboard/Dashboard';
const App = () => {
  return (
   
    <Router>
      <Routes>
      <Route path="/" element={<Home/>} />
      <Route path="/dashboard" element={<Dashboard />} />

      </Routes>
    </Router>
   

  )
}

export default App