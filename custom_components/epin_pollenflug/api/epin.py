import logging
import time
from datetime import timedelta
from typing import List

from aiohttp import ClientSession

from custom_components.epin_pollenflug.dto.epin_dto import LocationDto, PollenDto, SeasonDto

_LOGGER = logging.getLogger(__name__)


class Epin:
    __base_url: str = 'https://epin.lgl.bayern.de'
    __api_url: str = __base_url + '/api'

    def __init__(self, session: ClientSession):
        self._session = session

    async def get_locations(self) -> List[LocationDto]:
        """
            Retrieves a list of locations from the API.

            Returns:
                List[LocationDto]: A list of LocationDto objects representing the locations.

            Raises:
                Exception: If there is an error retrieving the locations.
        """
        try:
            async with self._session.get(self.__api_url + '/locations') as response:
                data = await response.json()
                return [LocationDto.from_dict(location) for location in data]
        except Exception as e:
            _LOGGER.error(f"Error retrieving locations: {e}")
            return []

    async def get_pollen(self) -> List[str]:
        """
        Method Name: get_pollen

        Description:
        This asynchronous method is used to retrieve pollen data from the specified API URL.
        It sends a GET request to the '/pollen' endpoint and returns the received data
        in JSON format as a list of strings.
        If there is an error retrieving the data, an empty list will be returned.

        Parameters:
        - None

        Return Type:
        List[str] - A list of strings representing the pollen data.

        Example Usage:
        pollen_data = await get_pollen()

        """
        try:
            async with self._session.get(self.__api_url + '/pollen') as response:
                data = await response.json()
                return data
        except Exception as e:
            _LOGGER.error(f"Error retrieving pollen: {e}")
            return []

    async def get_seasons(self) -> List[SeasonDto]:
        """
        Retrieve a list of seasons.

        This method sends a GET request to the API endpoint '/season' to retrieve the list of seasons.
        The response is expected to be in JSON format.
        The method then converts the JSON data into a list of SeasonDto objects.

        Returns:
            A list of SeasonDto objects representing the seasons.

        Raises:
            Exception: If there is an error retrieving the seasons.
        """
        try:
            async with self._session.get(self.__api_url + '/seasons') as response:
                data = await response.json()
                return [SeasonDto.from_dict(season) for season in data]
        except Exception as e:
            _LOGGER.error(f"Error retrieving seasons: {e}")
            return []

    async def get_pollen_data(self, locations: List[str], pollen: List[str]) -> List[PollenDto]:
        """
        Retrieve pollen data for specified locations and types of pollen.

        Args:
            locations (List[str]): A list of locations for which to retrieve pollen data.
            pollen (List[str]): A list of types of pollen to retrieve data for.

        Returns:
            List[PollenDto]: A list of PollenDto objects containing the retrieved pollen data.

        Raises:
            None.

        Example usage:
            locations = ['location1', 'location2']
            pollen = ['type1', 'type2']
            pollen_data = await get_pollen_data(locations, pollen)
        """
        try:
            now = time.time()
            earlier = now - timedelta(hours=3).seconds
            url = f'{self.__api_url}/measurements?locations={",".join(locations)}&pollen={",".join(pollen)}&from={earlier}&to={now}'

            async with self._session.get(url) as response:
                data = await response.json()
                return PollenDto.from_dict(data)
        except Exception as e:
            _LOGGER.error(f"Error retrieving pollen: {e}")
            return []