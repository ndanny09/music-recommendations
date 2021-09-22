import os
from dotenv import find_dotenv, load_dotenv
import requests
import base64
import json
import flask
import random

load_dotenv(find_dotenv()) #Environment variables
clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")

clientCredentials = f"{clientID}:{clientSecret}" #Spotify credentials & access token
clientCredentialsB64 = base64.b64encode(clientCredentials.encode())
authorizationURL = "https://accounts.spotify.com/api/token"
tokenData = {
    "grant_type": "client_credentials"
}
tokenHeaders = {
    "Authorization": f"Basic {clientCredentialsB64.decode()}"
}
authorizationResponse = requests.post(authorizationURL, data=tokenData, headers=tokenHeaders)
authorizationResponseData = authorizationResponse.json()
accessToken = authorizationResponseData['access_token']
headers = { 
    "Authorization": "Bearer " +accessToken
}

ids = ['1EqmdzkoxPJlQP039YoGCq', '4iJLPqClelZOBCBifm8Fzv', '7H55rcKCfwqkyDFH9wpKM6'] #Vivid Undress, Pierce the Veil, Christina Perri
queries = "?market=US" 
topSongs = []
randomSongs = []
for id in ids: #Artists' top track (US)
    endpoint = f"https://api.spotify.com/v1/artists/{id}/top-tracks"
    endpointQueries = f"{endpoint}{queries}"
    result = requests.get(url=endpointQueries, headers=headers)
    for x in result.json()['tracks']:
        topSongs.append(x['name'])
    randomSongs.append(topSongs[random.randint(0, len(topSongs)-1)])
print(randomSongs)

##app = flask.Flask(__name__)

##@app.route("/")
##def index():
##    return flask.render_template("index.html")

##app.run(
##    debug=True
##)