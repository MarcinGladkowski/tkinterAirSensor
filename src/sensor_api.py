import requests

class ApiSensorClient:

    url = 'http://80.211.160.135:8000/api/sensor'

    def get_measure(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            print("Api error")
        else:
            return response.json()[0]