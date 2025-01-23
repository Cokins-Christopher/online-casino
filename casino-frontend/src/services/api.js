import axios from 'axios';

const API = axios.create({
    baseURL: 'http://localhost:8000/api',
    headers: {
        'Content-Type': 'application/json'
    }
});

export const fetchGames = async () => {
    const response = await API.get('/games/');
    return response.data;
};

export const placeBet = async (betDetails) => {
    const response = await API.post('/bets/', betDetails);
    return response.data;
};
