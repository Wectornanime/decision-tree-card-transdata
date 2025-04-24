import React, { useEffect, useRef, useState } from "react";
import { Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from 'chart.js';

import { api } from "../services/api";
import './DashboardPage.css'
import { getStatsResponse } from "../types/dashboardType";
import { Backdrop, CircularProgress } from "@mui/material";

ChartJS.register(ArcElement, Tooltip, Legend);

export default function DashboardPage() {
  const [stats, setStats] = useState<getStatsResponse | null>(null)
  const [datasetData, setDatasetData] = useState<any>([0, 0])
  const socketRef = useRef(null);

  async function fetchStats() {
    try {
      const { data } = await api.get('/predict')

      setStats(data)
      setDatasetData([data.classes["0"], data.classes["1"]])
    } catch (error) {
      console.log(error)
    }
  }

  useEffect(() => {
    // Conecta ao servidor WebSocket
    socketRef.current = new WebSocket(`${import.meta.env.VITE_WEBSOCKET_URL}/ws/predict`);

    socketRef.current.onopen = () => {
      console.log('Conectado!');
    };

    socketRef.current.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setStats(data)
      setDatasetData([data.classes["0"], data.classes["1"]])
    };

    // Limpa a conexão ao desmontar o componente
    return () => {
      socketRef.current.close();
    };
  }, []);

  const chartData = {
    labels: ["Não Fraude (0)", "Fraude (1)"],
    datasets: [
      {
        label: "Distribuição das predições",
        data: datasetData,
        backgroundColor: ["#4caf50", "#f44336"]
      }
    ]
  };

  return (
    <>
      <Backdrop open={!stats} sx={{ color: "#fff", zIndex: 9999 }}>
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

      {stats && (
        <div className="container">
          <h1>Dashboard</h1>
          <h2>Total de Previsões: {stats.total}</h2>
          <main>
            <section className="left">
              <div className="graph">
                <Pie data={chartData} />
              </div>
            </section>
            <section className="right">
              <h3>Médias das Features:</h3>
              <div className="features">
                <ul>
                  <li>Valor médio das transições: {stats.medias.ratio_to_median_purchase_price.toFixed(2)}</li>
                  <li>Distância de casa: {stats.medias.distance_from_home.toFixed(2)} km</li>
                  <li>Distância da última transação: {stats.medias.distance_from_last_transaction.toFixed(2)} km</li>
                </ul>
              </div>
            </section>
          </main>
        </div>
      )}
    </>
  )
}
