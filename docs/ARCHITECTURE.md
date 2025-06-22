# ICT Ultra Platform – Mimari Genel Bakış

```
+-------------------------+       HTTP      +-------------------------+
|      Dashboard (Next)   |  <------------> |     Gateway Service     |
|  Port 3000              |                |  FastAPI - Port 8000    |
+-------------------------+                +-----------+-------------+
                                                |   HTTP / JSON
                                                v
                                        +---------------------------+
                                        |       MT5 Service         |
                                        |   FastAPI - Port 8001     |
                                        +-----------+---------------+
                                                    |  MetaTrader5  IPC
                                                    v
                                        +---------------------------+
                                        |   MetaTrader 5 Terminal   |
                                        |  Tickmill-Demo Server     |
                                        +---------------------------+
```

## Bileşenler

| Katman | Açıklama |
|--------|----------|
| Dashboard (Next.js) | Kullanıcı arayüzü. Hesap girişi, manuel emir, pozisyon takibi. |
| Gateway Service | Tek giriş noktası. API-Key doğrulaması uygulanır, isteği ilgili mikro-servise yönlendirir. |
| MT5 Service | MetaTrader5 Python kütüphanesi ile gerçek terminale bağlanır, emir gönderir, pozisyon/hesap bilgisi döner. |
| MetaTrader 5 Terminal | Windows uygulaması, Tickmill-Demo sunucusuna bağlıdır. |

## Veri Akışı
1. Kullanıcı Dashboard üzerinden **/connect** çağrısı yapar.
2. Gateway, isteği MT5 Service'e ileterek oturumu başlatır.
3. Başarılıysa Dashboard, **/trade** veya **/positions** çağrılarını yapar.
4. Gateway bu çağrıları MT5 Service'e proxy'ler.
5. MT5 Service, MetaTrader terminali ile IPC üzerinden iletişim kurar ve sonucu geri döndürür.

## Portlar
| Bileşen | Port |
|---------|------|
| Gateway | 8000 |
| MT5 Service | 8001 |
| Dashboard | 3000 |

## Docker Compose
Tüm bileşenler `docker-compose.dev.yml` ile tek komutla ayağa kalkar:
```bash
pnpm dev:up        # veya   docker compose -f docker-compose.dev.yml up -d
```

## Güvenlik
- Tüm istekler `X-API-KEY` başlığı ile kimliklenir.
- Gateway, oran sınırlaması (rate-limit) uygular.

---
Bu dosya her mimari değişiklikte güncellenecektir. 