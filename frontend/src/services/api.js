import axios from "axios";

const API = axios.create({
  baseURL: "https://gembid-backend-kj2a.onrender.com",
});

export default API;
