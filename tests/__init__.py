import asyncio
import aiohttp
from custom_components.epin_pollenflug.api.epin import Epin


async def bootstrap():
    httpclient = aiohttp.ClientSession()

    epin = Epin(httpclient)

    locations = await epin.get_locations()
    pollen = await epin.get_pollen()
    seasons = await epin.get_seasons()
    pollen_data = await epin.get_pollen_data([[location.id for location in locations][0]], [pollen[0]])
    dashboard = {
        "locations": locations,
        "pollen": pollen,
        "seasons": seasons,
        "pollen_data": pollen_data
    }
    print(dashboard)

    await httpclient.close()


asyncio.run(bootstrap())
