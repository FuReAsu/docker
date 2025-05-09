from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Simulated encryption/decryption (for demonstration)
def fake_decrypt(encrypted_text: str) -> str:
    try:
        print(f"/decrypt -> Received: {encrypt_text}")
        append=" decrypted"
        return encrypted_text+append  
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid encrypted data")

def fake_encrypt(unencrypted_text: str) -> str:
    try:
        print(f"/encrypt -> Received: {encrypt_text}")
        append=" encrypted"
        return unencrypted_text+append
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invaid data")

class EncryptedText(BaseModel):
    data: str

class UnencryptedText(BaseModel):
    data: str

@app.post("/decrypt")
def decrypt_text(payload: EncryptedText):
    decrypted = fake_decrypt(payload.data)
    return {"data": decrypted}

@app.post("/encrypt")
def encrypt_text(payload: UnencryptedText):
    encrypted = fake_encrypt(payload.data)
    return {"data": encrypted}

@app.get("/")
def info():
    return {"app": "fake cryptography module", "paths": ["/encrypt","/decrypt"]}

