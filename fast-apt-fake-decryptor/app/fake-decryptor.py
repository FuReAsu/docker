from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Simulated encryption/decryption (for demonstration)
def fake_decrypt(encrypted_text: str) -> str:
    try:
        return encrypted_text[::-1]  # Just reverses the string
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid encrypted data")

class EncryptedText(BaseModel):
    data: str

@app.post("/decrypt")
def decrypt_text(payload: EncryptedText):
    decrypted = fake_decrypt(payload.data)
    return {"decrypted": decrypted}
