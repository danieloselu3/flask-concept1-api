# Flask API Server
A Flask API server that can take an incoming POST request.

This is a sample Flask API that provides basic functionality for managing user data. The API supports both GET and POST requests to interact with user data.

## Getting Started
Before running the API, make sure you have the environment running and the required packeges are installed. 

### Setting Up the Environment
Once the repository has been cloned to your local space, cd into the folder,then using your favorite command line, install Virtualenv if you haven't, and create a new virtual environment **(Following instructions assume you have python installed in your system)**.

on Gitbash or Terminal, this can be done using the command:

```bash
pip install virtualenv
virtualenv flask_server_api_venv
```

Once installed and created, activate the virtual environment, this can be done using the command:
```bash
source flask_server_api_venv/Scripts/activate
```

You can then use the requirements.txt file to install the required packages. Do this using the command:
```bash
pip install -r requirements.txt
```

## Usage
To run our main Python Script, run the code:
```bash
python app.py
```
This will run the flask app server programmatically in debug mode.

## API Endpoints
* GET /v1/: Retrieves a list of user data in JSON format. Returns a 404 status code if there are no users.
* POST /v1/: Adds a new user to the user data list. Requires 'user' and 'prompt' fields in the form data. Returns the updated user data in JSON format with a 201 status code.

## License
This code is released under the MIT LICENSE

