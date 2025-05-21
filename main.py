from fastapi import FastAPI
import uvicorn

app = FastAPI()

# An API endpoint is a point of interaction between a client and a server.
# An API endpoint is also a route that the client can call to perform a specific action.
# its composed of a URL and an HTTP method (GET, POST, PUT, DELETE etc)

@app.get('/')
def home():
    return {'Data': 'Test'}