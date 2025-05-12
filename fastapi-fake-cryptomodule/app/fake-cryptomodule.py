from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

app = FastAPI()

# Simulated encryption/decryption (for demonstration)
def fake_decrypt(encrypted_text: str) -> str:
    try:
        append=" decrypted"
        return encrypted_text+append  
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid encrypted data")

def fake_encrypt(unencrypted_text: str) -> str:
    try:
        append=" encrypted"
        return unencrypted_text+append
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invaid data")

class EncryptedText(BaseModel):
    data: str

class UnencryptedText(BaseModel):
    data: str

@app.post("/decrypt")
def decrypt_text(payload: EncryptedText, response: Response):
    print(f"/decrypt -> Received: {payload.data}")
    decrypted = fake_decrypt(payload.data)
    print(f"/decrypt -> Response: {decrypted}")
    response.headers["Access-Control-Allow-Origin"] = "*"
    return {"data": decrypted}

@app.post("/encrypt")
def encrypt_text(payload: UnencryptedText, response: Response):
    print(f"/encrypt -> Received: {payload.data}")
    encrypted = fake_encrypt(payload.data)
    print(f"/encrypt -> Response: {encrypted}")
    response.headers["Access-Control-Allow-Origin"] = "*"
    return {"data": encrypted}

@app.get("/")
def info():
    return {"app": "fake cryptography module", "paths": ["/encrypt","/decrypt"]}

