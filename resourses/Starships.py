from ApiBase import ApiBase
from urllib.parse import urljoin
from robot.api.deco import *

STARSHIPS_PATH = 'starships/'


class Starships(ApiBase):
    def __init__(self):
        starships_url = urljoin(self.ENDPOINT, STARSHIPS_PATH)
        super().__init__(starships_url)

    @keyword(name="Get Starship")
    def get_starship(self, starship_id, expected_code=200):
        url = urljoin(self.api_url, starship_id)
        return self.session_request('GET', url, expected_code=expected_code).json()