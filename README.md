# TikTok API Server

A FastAPI server that uses TikTokApi to fetch video info and related videos.

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/jiscaskalov/tiktok-api-server.git
cd tiktok-api-server
```

### 2. Configure Environment

```bash
cp .env.example .env
nano .env
```
Edit .env if you want to change the browser used and number of sessions.

### Docker (Reccomended)

Run `docker-compose up --build`.
Server will be on port 8000.

### Manual

1. Make sure Python 3.12+ is installed.
2. Install Python dependencies: `pip install -r requirements.txt`.
3. Install Playwright:
```bash
python -m playwright install-deps
python -m playwright install
```

4. Start server: `uvicorn main:app --host 0.0.0.0 --port 8000`.

## Usage

- `GET /video_info?url=<Video URL>` -> returns video info
- `GET /related_videos?url=<Video URL>&count=<number>` -> returns related videos
- `GET /author_info?url=<User URL>` -> returns author info
