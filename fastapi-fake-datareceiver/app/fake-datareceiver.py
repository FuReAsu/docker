from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    data: str

@app.post("/write")
def write_data(payload: Message):
    # Write to a file
    with open("received_data.txt", "a") as f:
        f.write(payload.data + "\n")

    # Optionally print to console
    print(f"Received: {payload.data}")

    return {"status": "written", "received": payload.data}
