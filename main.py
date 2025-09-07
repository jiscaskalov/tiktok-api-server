from fastapi import FastAPI, HTTPException, Query
from sessions import init_sessions, get_api
import random

app = FastAPI(title="TikTok API Server")

@app.on_event("startup")
async def startup_event():
    await init_sessions()

@app.get("/video_info")
async def video_info(url: str = Query(...)):
    api = await get_api()
    try:
        session_index = random.randint(0, len(api.sessions) - 1)
        video = api.video(url=url, session_index=session_index)
        info = await video.info()
        print(f"[REQ] video_info using session {session_index}")
        return info
    except Exception as e:
        print(f"[ERR] video_info using session {session_index}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/related_videos")
async def related_videos(url: str = Query(...), count: int = 5):
    api = await get_api()
    try:
        session_index = random.randint(0, len(api.sessions) - 1)
        video = api.video(url=url, session_index=session_index)
        related = []
        async for vid in video.related_videos(count=count):
            related.append(vid.as_dict)
        print(f"[REQ] related_videos using session {session_index}")
        return {"related_videos": related}
    except Exception as e:
        print(f"[ERR] related_videos using session {session_index}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/author_info")
async def author_info(url: str = Query(...)):
    api = await get_api()
    try:
        session_index = random.randint(0, len(api.sessions) - 1)
        video = api.video(url=url, session_index=session_index)
        info = await video.info()
        author = info.get("author")
        print(f"[REQ] author_info using session {session_index}")
        return author
    except Exception as e:
        print(f"[ERR] author_info using session {session_index}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/video_stream")
async def video_bytes(url: str = Query(...)):
    api = await get_api()
    try:
        session_index = random.randint(0, len(api.sessions) - 1)
        video = api.video(url=url, session_index=session_index)
        data = await video.bytes()
        print(f"[REQ] video_bytes using session {session_index}")
        return {"video_bytes_length": len(data)}
    except Exception as e:
        print(f"[ERR] video_bytes using session {session_index}")
        raise HTTPException(status_code=500, detail=str(e))
