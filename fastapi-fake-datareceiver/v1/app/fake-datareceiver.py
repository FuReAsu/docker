from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    data: str

@app.post("/write")
def write_data(payload: Message,response: Response):
    # Write to a file
    with open("received_data.txt", "a") as f:
        f.write(payload.data + "\n")

    # Optionally print to console
    print(f"Received: {payload.data}")
    data = f"written {payload.data}"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return {"data": data}

@app.get("/")
def info():
    return {"app": "fake data receiver", "paths": ["/write","/read"]}

@app.get("/read")
def read_data(response: Response):
    with open("received_data.txt","r") as f:
        data = f.read()
    print("read data from the data file")
    response.headers["Access-Control-Allow-Origin"] = "*"
    return {"data": data}