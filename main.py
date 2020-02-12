import logging
import sys

from livetweets.web import make_app




logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = make_app()


