from ApiBase import ApiBase
from urllib.parse import urljoin
from robot.api.deco import *

PEOPLE_PATH = 'people/'


class People(ApiBase):
    def __init__(self):
        people_url = urljoin(self.ENDPOINT, PEOPLE_PATH)
        super().__init__(people_url)

    @keyword(name="Get Person")
    def get_person(self, person_id, expected_code=200, get_response_obj=False):
        url = urljoin(self.api_url, person_id)
        if get_response_obj:
            return self.session_request('GET', url, expected_code=expected_code)
        else:
            return self.session_request('GET', url, expected_code=expected_code).json()
