const express = require('express');
const axios = require('axios');
require('dotenv').config();
const app = express();
const PORT = process.env.PORT;

/* Weather get endpoint
    @Params: City
    @Returns: JSON weather data 
    @Description: 
    - Use OpenWeatherMap weather api with given city to get weather data as json
*/
app.get('/weather', async (req, res) => {
  const city = req.query.city;
  if ( !city ) // validate city param
    return res.status(400).send('Parameter {city} is missing')
  
  // attempt retrieve weather json data - report error code and messsage on fail
  try { 
    const cityWeatherData = await getWeatherByCity(city)
    res.send(cityWeatherData);
  } catch (error) {
    console.error('Error fetching weather data:', error.response ? error.response.data : error.message);
    res.status(500).send('Error fetching weather data: ' + error.response ? error.response.data : error.message)
  }
});

// Request to OpenWeatherMap weather api given city
const getWeatherByCity = async (city) => {
  try{
    const cityWeatherResponse = await axios.get(process.env.Weather_API_URL, {
        params: {
            q: city,
            appid: process.env.API_KEY
        }
    });
    return cityWeatherResponse.data
  } catch (error) {
    throw error
  }
}

// Start server on port 3000
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`)
});