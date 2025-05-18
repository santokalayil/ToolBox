from typing import Literal
import httpx
from .__config import GOOGLE_API_KEY


async def get_weather_data_raw(longitude: float, latitude: float) -> dict:
    """Fetches the current weather data for a specific geographical location using the Google Weather API.
    Args:
        longitude (float): The longitude of the location for which weather data is to be retrieved.
        latitude (float): The latitude of the location for which weather data is to be retrieved.
    Returns:
        dict: A dictionary containing the current weather data for the specified location.
    Raises:
        httpx.HTTPStatusError: If the HTTP request to the Google Weather API fails or returns an error status.
    """
    params = {
        "key": GOOGLE_API_KEY,
        "location.latitude": latitude,
        "location.longitude": longitude,
    }
    url = "https://weather.googleapis.com/v1/currentConditions:lookup"
    async with httpx.AsyncClient() as client:
        res = await client.get(url, params=params)
        res.raise_for_status()
        return res.json()

async def get_weather_forecast_raw(longitude: float, latitude: float, frequency: Literal["day"]) -> dict:
    """
    Fetches the raw weather forecast data for a specific location using the Google Weather API.

    Args:
        longitude (float): The longitude of the location for which the weather forecast is requested.
        latitude (float): The latitude of the location for which the weather forecast is requested.
        frequency (Literal["day"]): The frequency of the forecast. Currently, only "day" is supported.

    Returns:
        dict: The raw JSON response containing the weather forecast data.

    Raises:
        httpx.HTTPStatusError: If the HTTP request to the Google Weather API fails.

    Note:
        - Ensure that the `GOOGLE_API_KEY` is set and valid.
        - The API endpoint and parameters are subject to change based on the Google Weather API's documentation.
    """
    params = {
        "key": GOOGLE_API_KEY,
        "location.latitude": latitude,
        "location.longitude": longitude,
    }
    url = f"https://weather.googleapis.com/v1/forecast/{frequency}s:lookup"
    async with httpx.AsyncClient() as client:
        res = await client.get(url, params=params)
        res.raise_for_status()
        return res.json()



if __name__ == "__main__":
    longitude = -122.0838
    latitude = 37.3861
    weather_data = get_weather_data_raw(longitude, latitude)
