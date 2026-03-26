import requests
from endpoint.base_endpoint import Endpoint


class UpdateObject(Endpoint):

    def update_by_id(self, obj_id, payload):
        self.response = requests.put(
        f'https://api.restful-api.dev/objects/{obj_id}',
        json = payload
        )
        self.response_json = self.response.json()

    def check_response_year(self, year):
        assert self.response_json["data"]["year"] == year

    def check_response_price(self, price):
        assert self.response_json["data"]["price"] == price

    def check_response_cpu_model(self, cpu_model):
        assert self.response_json["data"]["CPU model"] == cpu_model