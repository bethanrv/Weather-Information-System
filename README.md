# Weather-Information-System
Simple REST API using Node.js that provides weather information for a given city, and a python script to consume that api.

## Instructions
- Setup for node.js server:
    - Install Node.js: Make sure you have Node.js installed on your system. Node.js can be installed here: https://nodejs.org/.
    - Clone Git Repo: Use the following command to clone the Weather-Information-System repo to your machine.
        - git clone https://github.com/bethanrv/Weather-Information-System.git
    - Install npm: Use the following command to inside the Weather-Information-System directory.
        - npm install
    - Start the Server: Once everything is installed, you can run the server via the following command. This will start the server on localhost:3000
        - npm start
- Setup for python client:
    - Install Python: Make sure you have Python installed on your system. Python can be installed from the windows store or from https://www.python.org/.
    - Install requests library: requests is the only external dependency and can be installed with the following command.
        - pip install requests
    - Run the Python Client: Once everything is installed, navigate to the Weather-Information-System directory on your machine and run the following command to start the program.
        - python client.py
    - Using client.py: Simply type the name of the city you would like to know the weather for, and type exit when you would like to close the program.

## Client Assumptions (client.py)
- Requests Library: The program utilized the python requests library found at https://pypi.org/project/requests/. Users should use pip to install the requests library before attempting to execute the script.
- Python Version: The python requests library officially supports python versions 3.7+. Users should run client.py with python version 3.7 or higher.
- API Endpoint: The program assumes that the Weather API is accessible at the specified API_URL (http://localhost:3000/weather?city=).
- Data Format: The program expects the weather data returned by the API in JSON format
- Error Handling: The error handling checks in the script assumes certain error conditions and responses from the Node.js Weather API. For example, it checks if the status code is 200 for successful requests and looks for specific error messages like 'city not found' or a status code of 500 for internal server issues.
- User Input: The program expects the user to input city names to request weather data.

## Server Assumptions (app.js)
- Express Installed: The script assumes that Express.js is installed in the environment where it is being executed.
- Axios Installed: The script assumes that Axios is installed in the environment where it is being executed.
- OpenWeatherMap API Access: The script assumes that the OpenWeatherMap API is accessible at the URL specified in .env.
- Request Parameters: The /weather endpoint expects a city parameter in the query string of the request. It assumes that the client will provide the city parameter to fetch weather data for a specific city.
- JSON Response Format: The script assumes that the successful response from the OpenWeatherMap API will be in JSON format and contain the necessary weather data.