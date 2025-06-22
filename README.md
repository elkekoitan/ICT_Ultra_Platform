# 🚀 ICT Ultra Platform - Python Edition

> **Ultra-fast Professional Trading Platform with Advanced AI & Machine Learning**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## ✨ Özellikler

### 🔥 Temel Özellikler
- **Ultra-hızlı İşlem Yürütme**: Sub-milisaniye tepki süreleri
- **Gelişmiş ICT Analizi**: Order Blocks, Fair Value Gaps, Liquidity Zones
- **AI-Powered Tahminler**: Machine Learning ile piyasa analizi
- **Real-time WebSocket**: Canlı veri akışı ve işlem yürütme
- **MT5 Entegrasyonu**: Doğrudan broker bağlantısı
- **Multi-Asset Support**: Forex, Crypto, Stocks, Commodities

### 🤖 AI & Machine Learning
- **Prophet Forecasting**: Facebook'un gelişmiş tahmin modeli
- **LSTM Neural Networks**: Derin öğrenme ile fiyat tahmini
- **Sentiment Analysis**: Piyasa duygu analizi
- **Pattern Recognition**: Otomatik grafik deseni tanıma
- **Risk Management AI**: Akıllı risk yönetimi algoritmaları

### 📊 Gelişmiş Analiz
- **Smart Money Concepts**: Institutional flow analizi
- **Market Structure**: BOS, CHoCH, MSS detection
- **Volume Profile**: Professional seviye hacim analizi
- **Fibonacci Extensions**: Otomatik Fibonacci seviyeleri
- **Support/Resistance**: AI-powered S/R seviyeleri

### 🏗️ Teknik Özellikler
- **Async/Await**: Modern Python async programlama
- **FastAPI**: Ultra-hızlı REST API
- **WebSocket**: Real-time bidirectional communication
- **PostgreSQL**: Enterprise-grade veritabanı
- **Redis**: High-performance caching
- **Docker**: Containerized deployment

## 🚀 Hızlı Başlangıç

### Gereksinimler
- Python 3.11+
- PostgreSQL 14+
- Redis 7+
- MetaTrader 5 (MT5 entegrasyonu için)

### Kurulum

1. **Repository'i klonlayın**
```bash
git clone https://github.com/ict-ultra/platform.git
cd platform
```

2. **Virtual environment oluşturun**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# veya
venv\Scripts\activate  # Windows
```

3. **Bağımlılıkları yükleyin**
```bash
pip install -r requirements.txt
```

4. **Environment variables ayarlayın**
```bash
cp .env.example .env
# .env dosyasını düzenleyin
```

5. **Veritabanını başlatın**
```bash
alembic upgrade head
```

6. **Uygulamayı çalıştırın**
```bash
uvicorn src.ict_ultra.main:app --reload --host 0.0.0.0 --port 8000
```

## 📚 API Dokümantasyonu

Uygulama çalıştırıldıktan sonra:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🏛️ Mimari

```
src/ict_ultra/
├── core/           # Temel konfigürasyon ve ayarlar
├── api/            # FastAPI route'ları ve endpoints
├── models/         # SQLAlchemy modelleri
├── services/       # İş mantığı servisleri
├── trading/        # Trading engine ve stratejiler
├── analysis/       # ICT analiz algoritmaları
├── ml/             # Machine Learning modelleri
├── websocket/      # WebSocket handlers
└── utils/          # Yardımcı fonksiyonlar
```

## 🔧 Konfigürasyon

### Environment Variables

```env
# Database
DATABASE_URL=postgresql://user:password@localhost/ict_ultra
REDIS_URL=redis://localhost:6379

# Trading
MT5_LOGIN=your_mt5_login
MT5_PASSWORD=your_mt5_password
MT5_SERVER=your_mt5_server

# API Keys
ALPHA_VANTAGE_API_KEY=your_api_key
POLYGON_API_KEY=your_api_key

# Security
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 📈 Trading Strategies

### ICT Concepts
- **Order Blocks**: Institutional order clustering
- **Fair Value Gaps**: Imbalance areas
- **Liquidity Zones**: High-volume areas
- **Smart Money Index**: Institutional flow indicator

### AI Strategies
- **LSTM Price Prediction**: Deep learning forecasting
- **Sentiment-Based Trading**: News sentiment analysis
- **Pattern Recognition**: Automated chart patterns
- **Risk-Adjusted Portfolios**: AI-optimized allocation

## 🔌 WebSocket API

### Bağlantı
```javascript
const socket = io('ws://localhost:8000');
```

### Events
```javascript
// Market data subscription
socket.emit('subscribe_market_data', {
    symbols: ['EURUSD', 'GBPUSD', 'USDJPY']
});

// Trade execution
socket.emit('execute_trade', {
    symbol: 'EURUSD',
    type: 'buy',
    volume: 0.1,
    price: 1.0850
});

// ICT analysis subscription
socket.emit('subscribe_ict_analysis', {
    symbols: ['EURUSD'],
    timeframes: ['1H', '4H', '1D']
});
```

## 🧪 Testing

```bash
# Tüm testleri çalıştır
pytest

# Coverage ile
pytest --cov=src/ict_ultra

# Sadece unit testler
pytest -m unit

# Sadece integration testler
pytest -m integration
```

## 🐳 Docker Deployment

```bash
# Build
docker build -t ict-ultra-platform .

# Run
docker-compose up -d
```

## 📊 Monitoring

### Prometheus Metrics
- Request latency
- Trade execution times
- WebSocket connections
- Database query performance

### Grafana Dashboards
- Trading performance
- System metrics
- User activity
- Error rates

## 🔒 Security

- **JWT Authentication**: Secure API access
- **Rate Limiting**: API abuse protection
- **Input Validation**: Pydantic models
- **SQL Injection Protection**: SQLAlchemy ORM
- **CORS Configuration**: Cross-origin security

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- 📧 Email: support@ictultra.com
- 💬 Discord: [ICT Ultra Community](https://discord.gg/ictultra)
- 📖 Documentation: https://docs.ictultra.com
- 🐛 Issues: https://github.com/ict-ultra/platform/issues

## 🙏 Acknowledgments

- ICT Trading Concepts by Michael J. Huddleston
- FastAPI by Sebastián Ramirez
- Python Trading Community
- Open Source Contributors

---

**⚡ Built with ❤️ for Professional Traders** 

### Hızlı Servis Başlatma (Windows)
```
:: MT5 servisi
scripts\start_mt5_service.bat

:: Gateway servisi (ayrı terminal)
scripts\start_gateway.bat
```
Servisleri durdurmak için:
```
scripts\stop_services.bat
``` 