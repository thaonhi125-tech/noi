import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import ReactGA from 'react-ga4';
import './index.css';
import App from './App.tsx';

// Initialize Google Analytics with the provided Measurement ID
const gaMeasurementId = 'G-R0LZL5XTQ0';
ReactGA.initialize(gaMeasurementId);

// Send a pageview event for the initial load
ReactGA.send({ hitType: "pageview", page: window.location.pathname });

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
