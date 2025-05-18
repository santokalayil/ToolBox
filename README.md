# ToolBox

ToolBox is a collection of tools and functions designed to be used in conjunction with Language Model (LLM) agents. This repository provides utilities for interacting with APIs, handling geolocation, weather data, and more. The tools are modular and can be easily integrated into larger projects.

## Features

- **Geolocation Tools**: Retrieve the current location and nearest address using Google APIs.
- **Weather Tools**: Fetch current weather data and forecasts for specific locations.
- **Modular Design**: Each tool is self-contained and can be used independently.
- **Asynchronous Support**: All API interactions are designed to be non-blocking using `httpx`.

## Folder Structure

```
ToolBox/
├── toolbox/               # Core toolbox module
│   ├── gcp/               # Google Cloud Platform tools
│   │   ├── location.py    # Geolocation tools
│   │   ├── weather.py     # Weather tools
```

## Getting Started

### Prerequisites

- Python 3.10 or higher
- A valid Google API Key for geolocation and weather tools

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/santokalayil/ToolBox.git
   cd ToolBox
   ```
2. Install dependencies:
    ```bash
    pip install uv
    uv install
    ```

3. Set up your Google API Key by creating a `.env` file in the appropriate directory. Use the `env.example` file as a reference. Then, edit the `.env` file to include your Google API Key:


### Usage

#### Geolocation Tools

```python
from toolbox.gcp.location import get_current_location_coordinates_raw, get_nearest_address_raw

# Example: Get current location coordinates
coordinates = await get_current_location_coordinates_raw()

# Example: Get nearest address
address = await get_nearest_address_raw(latitude, longitude)
```

#### Weather Tools

```python
from toolbox.gcp.weather import get_weather_data_raw, get_weather_forecast_raw

# Example: Get current weather data
weather_data = await get_weather_data_raw(longitude, latitude)

# Example: Get weather forecast
forecast = await get_weather_forecast_raw(longitude, latitude, frequency="day")
```

## Development Roadmap

We are currently focused on developing tools for Google Cloud Platform (GCP), including geolocation and weather utilities. Once the GCP tools are complete, we plan to expand the toolbox to include other functionalities such as Telegram bots, web scrapers, and more.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [httpx](https://www.python-httpx.org/) for asynchronous HTTP requests
- Google APIs for geolocation and weather data