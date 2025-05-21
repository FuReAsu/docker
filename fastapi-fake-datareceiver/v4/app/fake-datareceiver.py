from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json

app = FastAPI()

@app.post("/write")
async def write_data(request: Request):
    try:
        body = await request.json()

        payload_str = body.get("payload")
        if not isinstance(payload_str, str):
            return JSONResponse(content={"error": "'payload' must be a string"}, status_code=400)

        # Parse the inner JSON string
        payload_obj = json.loads(payload_str)

        # Add "Status": "Written"
        payload_obj["Status"] = "Written"

        # Stringify the modified payload again
        updated_payload_str = json.dumps(payload_obj)

        # Return the outer JSON with the updated stringified payload
        return {"payload": updated_payload_str}

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
