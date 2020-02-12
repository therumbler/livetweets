import logging
from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocket

from .livetweets import livetweets

logger = logging.getLogger(__name__)

def make_app():

    app = FastAPI()

    with open('static/index.html') as f:
        index_html = f.read()

    @app.get('/')
    async def index():
        return HTMLResponse(index_html)

    @app.websocket('/ws')
    async def websocket_endpoint(ws: WebSocket):
        await ws.accept()
        logger.info('ws connectoin')
        track = await ws.receive_text()
        logger.info('searching for %s', track)
        async for tweet in livetweets(track=track):
            logger.info(tweet)
            await ws.send_json(tweet)

    return app
