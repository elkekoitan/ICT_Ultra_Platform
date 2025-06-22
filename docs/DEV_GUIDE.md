# Geliştirici Kılavuzu

Bu kılavuz, ICT Ultra Platform Python mikro-servisleriyle çalışacak geliştiriciler için hazırlanmıştır.

## Gereksinimler
- Python 3.11+
- Node.js 20+ (dashboard için)
- Docker + Docker Compose
- MetaTrader 5 Windows terminali (Tickmill-Demo hesap bilgileriyle kurulu)

## Hızlı Başlangıç
```bash
# repo'yu klonla
$ git clone https://github.com/elkekoitan/ICT_Ultra_Platform.git
$ cd ICT_Ultra_Platform_Python

# sanal ortam
$ python -m venv .venv && source .venv/Scripts/activate
$ pip install -r requirements.txt

# MT5 terminal zaten açıksa servisleri başlat
$ uvicorn services.mt5_service.main:app --port 8001 &
$ uvicorn services.gateway.main:app --port 8000 &
```

## Docker ile
```bash
$ docker compose -f docker-compose.dev.yml up --build -d
```

## Test Çalıştırma
```bash
$ pytest -q
```
CI pipeline'ı GitHub Actions üzerinde pytest + Playwright testlerini otomatik çalıştırır.

## Yaygın Komutlar
| Amaç | Komut |
|------|-------|
| MT5'e bağlanma | `curl -X POST localhost:8000/connect -H "X-API-KEY: devkey" -d '{ ... }'` |
| Emir gönder | `curl -X POST localhost:8000/trade -H "X-API-KEY: devkey" -d '{ ... }'` |

## Versiyonlama
- Dal yapısı: `main` (production) / `dev` (güncel geliştirme)
- Commit mesaj şablonu: `Tx-y: kısa açıklama`

## Katkı Akışı
1. `git pull origin dev`
2. Yeni branch: `git checkout -b feature/short-desc`
3. Kod + test + `black` lint
4. `pytest && git commit -m ... && git push`
5. PR ➜ code review ➜ merge ➜ CI

---
Daha fazla detay için `docs/ARCHITECTURE.md` dosyasını inceleyin. 