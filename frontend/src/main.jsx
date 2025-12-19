import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import App from './App'
import Dashboard from './pages/Dashboard'
import TenderList from './pages/TenderList'
import TenderDetail from './pages/TenderDetail'

createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<App />}>
          <Route index element={<Dashboard/>} />
          <Route path='tenders' element={<TenderList/>} />
          <Route path='tenders/:id' element={<TenderDetail/>} />
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
)
