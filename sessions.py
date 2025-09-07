import asyncio
import os
from TikTokApi import TikTokApi

NUM_SESSIONS = int(os.getenv("NUM_SESSIONS", 5))
api_instance: TikTokApi = None

async def grab_token(session, index):
    await session.page.goto("https://www.tiktok.com")
    
    for _ in range(20):
        cookies = await api_instance.get_session_cookies(session)
        token = cookies.get("msToken")
        if token:
            session.ms_token = token
            print(f"[STR] Session {index+1} ms_token: {session.ms_token}")
            return
        await asyncio.sleep(0.5)
    
    print(f"[ERR] Session {index+1} get ms_token")

async def init_sessions():
    global api_instance
    api_instance = TikTokApi(logging_level="ERROR")
    
    await api_instance.create_sessions(
        num_sessions=NUM_SESSIONS,
        browser=os.getenv("TIKTOK_BROWSER", "chromium"),
        sleep_after=2
    )

    await asyncio.gather(*(grab_token(session, i) for i, session in enumerate(api_instance.sessions)))
    print(f"[STR] Created {NUM_SESSIONS} sessions.")

async def get_api() -> TikTokApi:
    global api_instance
    return api_instance
