import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import ReactGA from 'react-ga4';
import './index.css';
import App from './App.tsx';

// Initialize Google Analytics
// IMPORTANT: Replace G-YOUR_ID_HERE with your actual Measurement ID
const gaMeasurementId = 'G-YOUR_ID_HERE';
ReactGA.initialize(gaMeasurementId);

// Send a pageview event for the initial load
ReactGA.send({ hitType: "pageview", page: window.location.pathname });

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
