from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from humanizer import humanize

app = FastAPI(
    title="Text Humanizer API",
    description="API for rewriting text to sound more human-like using AI models.",
    version="1.0.0"
)

class HumanizeRequest(BaseModel):
    text: str
    style: str
    api_key: str
    model: str

class HumanizeResponse(BaseModel):
    output: str

@app.get("/")
def health():
    return {"status": "API is running"}

@app.post("/humanize", response_model=HumanizeResponse)
async def humanize_text(payload: HumanizeRequest):
    try:
        result = humanize(
            text = payload.text,
            style = payload.style,
            api_key = payload.api_key,
            model = payload.model
        )
        return HumanizeResponse(output=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))