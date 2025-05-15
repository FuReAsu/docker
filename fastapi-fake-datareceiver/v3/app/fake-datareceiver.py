from fastapi import FastAPI, Response, Request
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    id: str
    data: str

@app.post("/write")
def write_data(payload: Message, response: Response, request: Request):

    #Write id to a file
    with open ("received_id.txt", "a") as f:
        f.write(payload.id + "\n")

    # Write data to a file
    with open("received_data.txt", "a") as f:
        f.write(payload.data + "\n")

    # Optionally print to console
    print(f"Received: {payload.data}, From: {payload.id}")
    data = payload.data
    id = payload.id
    #set response header
    response.headers["Access-Control-Allow-Origin"] = "*"
    response_data = {"status": "written", "id" : id, "data": data}
    
    #get request headers and add them to the response
    headers = dict(request.headers)
    print(f"Request Headers: {headers}")
    response_data["request_headers"] = headers

    return response_data

@app.get("/")
def info():
    return {"app": "fake data receiver", "paths": ["/write","/read"]}

@app.get("/read")
def read_data(response: Response, request: Request):
    with open("received_data.txt","r") as f:
        data = f.read()
    with open("received_id.txt","r") as f:
        id = f.read()
    print("read data from the data files")
    response.headers["Access-Control-Allow-Origin"] = "*"
    response_data = {"id": id, "data": data}

    headers = dict(request.headers)
    print(f"Request Headers: {headers}")
    response_data["request_headers"] = headers

    return response_data