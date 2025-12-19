import { useEffect, useState } from "react";
import API from "../services/api";

export default function TenderList() {
  const [tenders, setTenders] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    API.get("/api/tenders")
      .then((res) => {
        setTenders(res.data);
      })
      .catch((err) => {
        console.error("Error loading tenders", err);
      })
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <p>Loading tenders...</p>;

  if (tenders.length === 0) {
    return <p>No tenders available yet.</p>;
  }

  return (
    <div>
      <h2>Available Tenders</h2>
      <ul>
        {tenders.map((t) => (
          <li key={t.id}>
            <strong>{t.title}</strong><br />
            <small>{t.description}</small>
          </li>
        ))}
      </ul>
    </div>
  );
}
