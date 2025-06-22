from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import MetaTrader5 as mt5
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="ICT Ultra MT5 Service", version="0.1.0")

class ConnectRequest(BaseModel):
    login: int
    password: str
    server: str
    path: str | None = None  # optional terminal path

class TradeRequest(BaseModel):
    symbol: str
    side: str  # BUY / SELL
    volume: float
    comment: str | None = "API Trade"

state = {
    "connected": False
}

def _connect(login: int, password: str, server: str, path: str | None = None):
    """MT5 terminale bağlan. Terminal zaten açıksa sadece initialize kullanılır.

    Args:
        login: Hesap numarası
        password: Şifre
        server: Sunucu adı
        path: İsteğe bağlı terminal yolu.
            * Bir dizin verilirse <dizin>/terminal64.exe otomatik eklenir.
            * Bir .exe dosyası verilirse doğrudan kullanılır.
    Returns:
        bool: Bağlantı başarılı mı
    """
    exe_path = None
    if path:
        # eğer path bir dizinse exe oluştur
        if path.lower().endswith(".exe"):
            exe_path = path
        else:
            exe_path = os.path.join(path, "terminal64.exe")
    try:
        if exe_path:
            ok_init = mt5.initialize(path=exe_path, login=login, password=password, server=server)
        else:
            ok_init = mt5.initialize(login=login, password=password, server=server)
    except Exception as ex:
        logger.exception("MT5 initialize failed: %s", ex)
        return False

    if ok_init:
        return True

    # Eğer initialize başarısız ama terminal halihazırda açıksa, ikinci bir deneme yap
    mt5.shutdown()
    if exe_path:
        mt5.initialize(path=exe_path)
    else:
        mt5.initialize()
    ok_login = mt5.login(login=login, password=password, server=server)
    return ok_login

@app.post("/connect")
def connect(req: ConnectRequest):
    if _connect(req.login, req.password, req.server, req.path):
        state["connected"] = True
        info = mt5.account_info()
        return {
            "success": True,
            "balance": info.balance,
            "currency": info.currency,
            "name": info.name,
            "login": info.login,
        }
    code, msg = mt5.last_error()
    return {"success": False, "error_code": code, "message": msg}

@app.get("/health")
def health():
    return {"status": "connected" if state["connected"] else "disconnected"}

@app.post("/trade")
def trade(req: TradeRequest):
    if not state["connected"]:
        return {"success": False, "error": "not connected"}
    order_type = mt5.ORDER_TYPE_BUY if req.side.upper()=="BUY" else mt5.ORDER_TYPE_SELL
    tick = mt5.symbol_info_tick(req.symbol)
    price = tick.ask if order_type==mt5.ORDER_TYPE_BUY else tick.bid
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": req.symbol,
        "volume": req.volume,
        "type": order_type,
        "price": price,
        "deviation": 20,
        "magic": 111000,
        "comment": req.comment,
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    result = mt5.order_send(request)
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        return {
            "success": True,
            "order": result.order,
            "deal": result.deal,
            "price": result.price,
            "timestamp": datetime.now().isoformat()
        }
    return {"success": False, "retcode": result.retcode, "comment": result.comment} 