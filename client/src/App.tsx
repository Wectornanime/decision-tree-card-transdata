import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import FormPage from './pages/FormPage';
import DashboardPage from './pages/DashboardPage';
import './App.css'

export default function App() {
  return (
    <Router>
      <nav>
        <Link to="/" style={{ marginRight: 10, fontWeight: 'bold', fontSize: "larger" }}>Formulário</Link>
        <Link to="/dashboard" style={{ marginRight: 10, fontWeight: 'bold', fontSize: "larger" }}>Dashboard</Link>
      </nav>
      <Routes>
        <Route path="/" element={<FormPage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
      </Routes>
    </Router>
  );
}
