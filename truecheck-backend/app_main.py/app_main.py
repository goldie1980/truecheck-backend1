

from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
client = OpenAI()

class ScanRequest(BaseModel):
    title: str | None = ""
    url: str | None = ""
    images: list[str] = []

@app.post("/api/v1/scan")
async def scan_product(req: ScanRequest):
    score = 100
    reasons = []

    text = (req.title or "").lower()

    if "100% authentic" in text:
        score -= 20
        reasons.append("Overuse of authenticity claims")
