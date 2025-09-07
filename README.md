# TikTok API Server

## Setup

### Docker

```bash
docker build -t tiktok-server .
docker run -p 8000:8000 tiktok-server
```

### Manual

1. Clone the repo
2. Copy `.env.example` to `.env` and edit if needed
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   playwright install
