from fastapi import FastAPI, HTTPException, Request, Depends
from pydantic import BaseModel
import httpx
import os

API_KEY = os.getenv("GATEWAY_API_KEY", "devkey")

async def verify_key(request: Request):
    key = request.headers.get("X-API-KEY")
    if key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")

app = FastAPI(title="ICT Ultra Gateway API", version="0.1.0")

class TradeRequest(BaseModel):
    symbol: str
    side: str  # BUY or SELL
    volume: float

@app.get("/health")
async def health() -> dict:
    """Gateway health-check"""
    return {"status": "ok"}

@app.post("/connect", dependencies=[Depends(verify_key)])
async def connect(req: dict):
    """Proxy connect request"""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                "http://mt5_service:8001/connect" if os.getenv("DOCKER") else "http://localhost:8001/connect",
                json=req,
            )
            return resp.json()
    except httpx.RequestError as exc:
        raise HTTPException(status_code=502, detail=f"mt5-service unreachable: {exc}")

@app.post("/trade", dependencies=[Depends(verify_key)])
async def trade(req: TradeRequest):
    """Proxy trade request to mt5-service"""
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                "http://mt5_service:8001/trade" if os.getenv("DOCKER") else "http://localhost:8001/trade",
                json=req.dict(),
            )
            return resp.json()
    except httpx.RequestError as exc:
        raise HTTPException(status_code=502, detail=f"mt5-service unreachable: {exc}") 