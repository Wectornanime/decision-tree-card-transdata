import React, { useState } from 'react'
import './FormPage.css'
import { api } from '../services/api';
import { Backdrop, Box, Button, CircularProgress, Dialog, DialogActions, DialogContent, DialogTitle, FormControlLabel, Radio, RadioGroup, Step, StepLabel, Stepper, TextField, Typography } from '@mui/material';
import { FormSteps } from '../assets/formSteps';
import { predictRequestType } from '../types/predictType';
import SmileyFace from '../assets/emojis/SmileyFace.gif';
import SadFace from '../assets/emojis/SadFace.gif';

function FormPage() {
  const [form, setForm] = useState<predictRequestType>({
    ratio_to_median_purchase_price: 0,
    online_order: 0,
    distance_from_home: 0,
    distance_from_last_transaction: 0
  });

  const [activeStep, setActiveStep] = useState(0)
  const [loading, setLoading] = useState(false);
  const [showForm, setShowForm] = useState(true);
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
  };

  const handleSubmit = async () => {
    try {
      setShowForm(false);
      setLoading(true);
      const response = await api.post('/predict', form);

      setResult(response.data);
    } catch {
      setResult({ erro: 'Erro ao conectar com a API' });
    } finally {
      setLoading(false);
    }
  };

  const handleDialogClose = () => {
    setResult(null);
    setShowForm(true);
    setActiveStep(0);
    setForm({
      ratio_to_median_purchase_price: 0,
      online_order: 0,
      distance_from_home: 0,
      distance_from_last_transaction: 0
    });
  };


  const stepForm = FormSteps[activeStep]

  return (
    <div className='container'>
      <h1>Detecção de Fraude</h1>

      <Stepper alternativeLabel activeStep={activeStep}>
        {FormSteps.map((step) => (
          <Step key={step.name}>
            <StepLabel>{step.label}</StepLabel>
          </Step>
        ))}
      </Stepper>

      {showForm && (
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
      )}

      <Backdrop open={loading} sx={{ color: "#fff", zIndex: 9999 }}>
        <React.Fragment>
          <svg width={0} height={0}>
            <defs>
              <linearGradient id="my_gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stopColor="#2CBEF1" />
                <stop offset="100%" stopColor="#61C56F" />
              </linearGradient>
            </defs>
          </svg>
          <CircularProgress sx={{ 'svg circle': { stroke: 'url(#my_gradient)' } }} />
        </React.Fragment>
      </Backdrop>

      <Dialog open={!!result} onClose={handleDialogClose}>
        <DialogTitle>Resultado da Predição</DialogTitle>
        <DialogContent>
          <pre>{result ? (result.prediction.value == '0' ? 'De acordo com os dados oferecidos sua transição não se intitula como não fraude.' : 'Lamentamos informar, mas sua transição se assemelha bastante a uma fraude.') : ''}</pre>
          <img
            src={result ? (result.prediction.value == '0' ? SmileyFace : SadFace) : ''}
            alt="Emoji"
            style={{ height: '150px', marginTop: '20px', marginLeft: 'auto', marginRight: 'auto', display: 'block' }}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleDialogClose}>Fechar</Button>
        </DialogActions>
      </Dialog>
    </div>
  )
}

export default FormPage
