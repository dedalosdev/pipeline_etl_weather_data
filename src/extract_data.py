import requests
import json
from pathlib import Path

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


api_key = '0fbcc15a242b57c1e21e3eee25cdb41b'
url = f'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={api_key}'

def extract_weather_data(url):
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        logging.error("Request error")
        return []

    if not data:
        logging.warn("No data returned")
        return []
        

    output_path = '../data/weather_data.json'
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

    logging.info(f"File saved in {output_path}")
    return data


extract_weather_data(url)