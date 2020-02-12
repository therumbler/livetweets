"""an Async generator that spits out live tweets"""
import asyncio
import logging

from .aiotwitter import stream

logger = logging.getLogger(__name__)


async def livetweets(track):
    """returns tweets for a given search"""

    async for tweet in stream(track=track):
        yield tweet

    logging.info('returning from livetweets generator')


