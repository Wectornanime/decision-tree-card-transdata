import { useState } from 'react'
import './FormPage.css'
import { api } from '../services/api';
import { Box, Button, FormControlLabel, Radio, RadioGroup, Step, StepLabel, Stepper, TextField, Typography } from '@mui/material';
import { FormSteps } from '../assets/formSteps';
import { predictRequestType } from '../types/predictType';

function FormPage() {
  const [form, setForm] = useState<predictRequestType>({
    ratio_to_median_purchase_price: 0,
    online_order: 0,
    distance_from_home: 0,
    distance_from_last_transaction: 0
  });

  const [activeStep, setActiveStep] = useState(0)

  const [result, setResult] = useState<any>(null);

  const handleNext = () => {
    if (activeStep === FormSteps.length - 1) {
      handleSubmit();
    } else {
      setActiveStep(prev => prev + 1);
    }
  };

  const handleBack = () => {
    if (activeStep !== 0) setActiveStep(prev => prev - 1);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleBooleanChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: parseInt(e.target.value) }); // 0 ou 1
    console.log(form);
  };

  const handleSubmit = async () => {
    try {
      const response = await api.post('/predict', form);

      setResult(response.data);
    } catch {
      setResult({ erro: 'Erro ao conectar com a API' });
    }
  };

  const stepForm = FormSteps[activeStep]

  return (
    <Box sx={{ width: '100%' }}>
      <h1>Detecção de Fraude</h1>

      <Stepper alternativeLabel activeStep={activeStep}>
        {FormSteps.map((step) => (
          <Step key={step.name}>
            <StepLabel>{step.label}</StepLabel>
          </Step>
        ))}
      </Stepper>

      <Box sx={{ p: 4, border: '1px solid #ccc', borderRadius: 2, mt: 2 }}>
        <Typography variant="h6">{stepForm.label}</Typography>
        <Typography variant="body2" sx={{ mb: 2 }}>{stepForm.description}</Typography>

        {stepForm.type === 'boolean' ? (
          <RadioGroup
            name={stepForm.name}
            value={form[stepForm.name]}
            onChange={handleBooleanChange}
            row
          >
            <FormControlLabel value="1" control={<Radio />} label="Sim" />
            <FormControlLabel value="0" control={<Radio />} label="Não" />
          </RadioGroup>
        ) : (
          <TextField
            fullWidth
            name={stepForm.name}
            value={form[stepForm.name]}
            onChange={handleChange}
            type="number"
            aria-valuemin={0}
          >
          </TextField>
        )}

        <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4, gap: 2 }}>
          <Button variant="contained" onClick={handleBack} disabled={activeStep === 0}>Voltar</Button>

          <Button variant="contained" onClick={handleNext}>
            {activeStep === FormSteps.length - 1 ? 'Enviar' : 'Próximo'}
          </Button>
        </Box>
      </Box>
    </Box>
  )
}

export default FormPage
