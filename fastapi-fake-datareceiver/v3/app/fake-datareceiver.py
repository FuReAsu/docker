from fastapi import FastAPI, Response, Request
from pydantic import BaseModel
import os

app = FastAPI()

class Message(BaseModel):
    name: str
    email: str

@app.post("/write")
def write_data(payload: Message, response: Response, request: Request):

    #Write id to a file
    with open ("received_id.txt", "a") as f:
        f.write(payload.name + "\n")

    # Write data to a file
    with open("received_data.txt", "a") as f:
        f.write(payload.email + "\n")

    # Optionally print to console
    print(f"Received: {payload.email}, From: {payload.name}")
    name = payload.name
    email = payload.email
    #set response header
    response.headers["Access-Control-Allow-Origin"] = "*"
    response_data = {"status": "written", "name" : name, "email": email}
    
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

    if not os.path.exists("received_data.txt") or not os.path.exists("received_id.txt"):
        return {"status": "data file doesn't exist yet"}

    with open("received_data.txt","r") as f:
        name = f.read()
    with open("received_id.txt","r") as f:
        email = f.read()

    name_list = name.split("\n")
    email_list = email.split("\n")
    
    list_length = len(name_list)

    response_list = []

    for i in range(0,list_length - 1):
        temp_item = {"name": name_list[i], "email": email_list[i]}
        response_list.append(temp_item) 
    

    print("read data from the data files")
    response.headers["Access-Control-Allow-Origin"] = "*"

    headers = dict(request.headers)
    print(f"Request Headers: {headers}")
   
    response_data = {"data": response_list, "headers": headers}

    return response_data
