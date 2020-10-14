from fastapi import FastAPI
from starlette.responses import RedirectResponse, Response

from dna import get_logs
from feed import generate_feed

app = FastAPI()

@app.get("/")
async def index():
    """
    Redirects to the docs.
    """
    return RedirectResponse(url="/logs")

@app.get("/logs")
async def logs(apps: str = '', level: str = '', to_time: str = '', from_time: str = '', size: int = 100):
    """
    Gets the logs as an XML RSS feed.
    """
    logs = get_logs(to_time=to_time, from_time=from_time, size=size, level=level, apps=apps)
    feed = generate_feed(logs)

    return Response(content=feed, media_type='application/xml')