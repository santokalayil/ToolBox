import json
import httpx

import nest_asyncio

from toolbox.gcp.weather import get_weather_data_raw, get_weather_forecast_raw
from toolbox.gcp.location import get_current_location_coordinates_raw, get_nearest_address_raw

nest_asyncio.apply()

async def main() -> None:
    # get_weather_data_raw(37.3861, -122.0838)
    coordinates = await get_current_location_coordinates_raw()
    lat, long = coordinates["location"]["lat"], coordinates["location"]["lng"]
    # this is based on the IP address

    # lat, long = 17.3850, 78.4867  # manual adding of location
    address_data = await get_nearest_address_raw(lat, long)
    address = address_data["results"][0]["formatted_address"]
    address

    # getting current weather data
    weather_data = await get_weather_data_raw(long, lat)
    weather_data
    # print(json.dumps(weather_data, indent=2))

    weatherforecast = await get_weather_forecast_raw(long, lat, frequency="day")
    weatherforecast


    data = {"address": address, "latitude": lat, "longitude": long, "weather": weather_data, "forecast": weatherforecast}
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

