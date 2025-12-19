import React, {useEffect, useState} from 'react'
import API from '../services/api'
import { Link } from 'react-router-dom'

export default function TenderList(){
  const [tenders, setT] = useState([])
  useEffect(()=>{
    API.get('/api/tenders').then(r=> setT(r.data)).catch(console.error)
  },[])
  return (
    <div>
      <h3>Tenders</h3>
      {tenders.length===0 && <p>No tenders yet.</p>}
      <ul>
        {tenders.map(t=> (
          <li key={t.id}><Link to={`/tenders/${t.id}`}>{t.title}</Link> — Score: {Math.round(t.score)}</li>
        ))}
      </ul>
    </div>
  )
}
