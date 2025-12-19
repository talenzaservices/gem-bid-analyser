import React, {useEffect, useState} from 'react'
import { useParams } from 'react-router-dom'
import API from '../services/api'

export default function TenderDetail(){
  const { id } = useParams()
  const [t, setT] = useState(null)
  useEffect(()=>{
    API.get('/api/tenders').then(r=>{
      const found = r.data.find(x=> x.id === Number(id))
      setT(found)
    })
  },[id])
  if(!t) return <div>Loading...</div>
  return (
    <div>
      <h3>{t.title}</h3>
      <p><strong>Score:</strong> {Math.round(t.score)}</p>
      <pre style={{whiteSpace:'pre-wrap'}}>{t.raw_text}</pre>
      <h4>Extracted</h4>
      <pre>{t.extracted}</pre>
    </div>
  )
}
