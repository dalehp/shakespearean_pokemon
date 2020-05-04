# shakespearean_pokemon
HTTP API to get Pokemon descriptions in a Shakespearean style

## Run the server
### Run Locally
First install Poetry https://python-poetry.org/docs/#installation (not recommended to use pip)
From top level of the repo:
```
> poetry install
> poetry run flask run
```
The server should now be running on localhost port 5000. 
You can then use the API, for example with httpie:
`http http://localhost:5000/porygon`
### Run in docker
Assuming docker is already installed.
```
> docker build . -t <choose a tag>
> docker run -d -p 5000:5000 <your tag>
```
You can then call the API as before.
