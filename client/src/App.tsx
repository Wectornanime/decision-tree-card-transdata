import { useState } from 'react'
import './App.css'
import { api } from './services/api';

function App() {
  const [form, setForm] = useState({
    ratio_to_median_purchase_price: '',
    online_order: '',
    distance_from_home: '',
    distance_from_last_transaction: ''
  })

  const [result, setResult] = useState<any>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await api.post('/predict', {
        ...form,
        ratio_to_median_purchase_price: parseFloat(form.ratio_to_median_purchase_price),
        online_order: parseInt(form.online_order),
        distance_from_home: parseFloat(form.distance_from_home),
        distance_from_last_transaction: parseFloat(form.distance_from_last_transaction)
      });
      setResult(response.data);
    } catch {
      setResult({ erro: 'Erro ao conectar com a API' });
    }
  };

  return (
    <div className='container'>
      <h1>Detecção de Fraude</h1>
      <form onSubmit={handleSubmit}>
        {Object.entries(form).map(([key, value]) => (
          <input
            key={key}
            name={key}
            value={value}
            onChange={handleChange}
            placeholder={key}
          />
        ))}
        <button type="submit">Enviar</button>
      </form>
      {result && (
        <div className='resultContainer'>
          <h2>Resultado:</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  )
}

export default App
