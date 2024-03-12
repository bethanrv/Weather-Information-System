const express = require('express');
const axios = require('axios');
require('dotenv').config();
const app = express();
const PORT = process.env.PORT;

// Weather get endpoint 
app.get('/weather', (req, res) => {
  const city = req.query.city;
  if ( !city ) // validate city param
    return res.status(400).send('Parameter {city} is missing.')
  res.send('test');
});

// Start server on port 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Request to OpenWeatherMap api
const getWeatherByCity = (city) => {
  /*
    example call:
        http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid={API key}
  */
  axios.get(process.env.API_URL)
  .then(response => {
      console.log('API Response:', response.data);
  })
  .catch(error => {
      console.error('Error fetching data:', error);
  });
}