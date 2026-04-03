import requests
import pandas as pd
from datetime import datetime

class DataCollector:
    def __init__(self, api_url):
        self.api_url = api_url

    def collect_data(self):
        response = requests.get(self.api_url)
        if response.status_code != 200:
            raise ValueError("Failed to fetch data from the API")
        return response.json()
    
    def validate_data(self, data):
        # Example validation: Check if required fields are present
        for match in data:
            if 'match_id' not in match or 'timestamp' not in match:
                return False
        return True
    
    def store_data(self, data, filename):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
    
    def preprocess_data(self, filename):
        df = pd.read_csv(filename)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)
        return df
