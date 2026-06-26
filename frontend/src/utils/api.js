import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  headers: {
    // We do not define the Content-type we let each function to define the header
    'Accept': 'application/json',
  },
})


api.interceptors.request.use((config) =>{
  const token = localStorage.getItem('token');
  if(token){
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
})

export default api


