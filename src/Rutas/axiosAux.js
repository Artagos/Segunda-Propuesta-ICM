import axios from 'axios';

const baseURL = process.env.NODE_ENV === 'production' ? 'https://back.dcubamusica.cult.cu/api/' : 'https://localhost:8000';

const http = axios.create({
    baseURL: baseURL,
    // other configuration options
});

export default http;
