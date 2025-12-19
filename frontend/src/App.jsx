import React from 'react'
import { Outlet, Link } from 'react-router-dom'

export default function App(){
  return (
    <div style={{fontFamily: 'Arial, sans-serif', padding: 20}}>
      <header style={{display:'flex', justifyContent:'space-between', alignItems:'center'}}>
        <h2>GeM Bid Analyser</h2>
        <nav>
          <Link to='/'>Dashboard</Link> | <Link to='/tenders'>Tenders</Link>
        </nav>
      </header>
      <main style={{marginTop:20}}>
        <Outlet />
      </main>
    </div>
  )
}
