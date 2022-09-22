from ApiBase import ApiBase
from urllib.parse import urljoin
from robot.api.deco import *

PLANETS_PATH = 'planets/'


class Planets(ApiBase):
    def __init__(self):
        planets_url = urljoin(self.ENDPOINT, PLANETS_PATH)
        super().__init__(planets_url)

    @keyword(name="Get Planet")
    def get_person(self, planet_id, expected_code=200):
        url = urljoin(self.api_url, planet_id)
        return self.session_request('GET', url, expected_code=expected_code).json()
