import httpx
import json

from .__config import GOOGLE_API_KEY

async def get_current_location_coordinates_raw() -> dict:
    """
    Get the current location of the device using Google Geolocation API.

    Returns:
        dict: A dictionary containing the current location coordinates.

    Raises:
        httpx.HTTPStatusError: If the HTTP request to the Google Geolocation API fails or returns an error status.

    Note:
        - Ensure that the `GOOGLE_API_KEY` is set and valid.
        - The API endpoint and parameters are subject to change based on the Google Geolocation API's documentation.
    """

    url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={GOOGLE_API_KEY}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "considerIp": True  # Request location based on the IP address
        # You can also provide information about wifiAccessPoints and cellTowers for more accuracy
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        return response.json()

async def get_nearest_address_raw(latitude: float, longitude: float) -> dict:
    """
    Retrieves the nearest address from Google Geocoding API for given coordinates.

    Args:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.
        api_key (str): Your Google Maps API key.

    Returns:
        str: The formatted address of the nearest location, or None if an error occurs.
    """
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "latlng": f"{latitude},{longitude}",
        "key": GOOGLE_API_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
        return response.json()

