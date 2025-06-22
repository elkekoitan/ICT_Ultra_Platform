from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx

app = FastAPI(title="ICT Ultra Gateway API", version="0.1.0")

class TradeRequest(BaseModel):
    symbol: str
    side: str  # BUY or SELL
    volume: float

@app.get("/health")
async def health() -> dict:
    """Gateway health-check"""
    return {"status": "ok"}

@app.post("/trade")
async def trade(req: TradeRequest):
    """Proxy trade request to mt5-service"""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post("http://localhost:8001/trade", json=req.dict())
            return resp.json()
    except httpx.RequestError as exc:
        raise HTTPException(status_code=502, detail=f"mt5-service unreachable: {exc}") 