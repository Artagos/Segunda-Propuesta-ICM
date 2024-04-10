import axios from 'axios';

const baseURL = process.env.NODE_ENV === 'production' ? 'https://dcubamusica.cult.cu/api/' : '';

const http = axios.create({
    baseURL: baseURL,
    // other configuration options
});

export default http;