import logging

from aiohttp import ClientSession

_LOGGER = logging.getLogger(__name__)


class Epin:
    def __init__(self, session: ClientSession):
        self._session = session

