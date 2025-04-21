import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import FormPage from './pages/Form';
import './App.css'

export default function App() {
  return (
    <Router>
      <nav>
        <Link to="/" style={{ marginRight: 10 }}>Formulário</Link>
        <Link to="/dashboard">Dashboard</Link>
      </nav>
      <Routes>
        <Route path="/" element={<FormPage />} />
      </Routes>
    </Router>
  );
}
