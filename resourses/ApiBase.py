import logging
import requests


class ApiBase:
    ENDPOINT = 'http://127.0.0.1:5000'

    def __init__(self, api_url):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.api_url = api_url
        self.session = requests.Session()
        self.session.headers['Content-Type'] = 'application/json;charset=utf-8'

    def session_request(self, method, url, payload=None, params=None,
                        headers=None, expected_code=200, **kwargs):

        response = self.session.request(method, url, headers=headers,
                                        json=payload, params=params, **kwargs)

        all_headers = self.session.headers
        if headers:
            all_headers.update(dict(headers))

        self.logger.info(f'REQUEST: {method} {url}')
        self.logger.info(f'REQUEST PAYLOAD: {payload}')
        self.logger.info(f'REQUEST PARAMS: {params}')
        self.logger.info(f'REQUEST HEADERS: {all_headers}')
        self.logger.info(f'RESPONSE STATUS CODE: {response.status_code}')
        self.logger.info(f'RESPONSE HEADERS: {response.headers}')
        self.logger.info(f'RESPONSE: {response.text}')

        assert response.status_code == int(expected_code), \
            f'Unexpected response status code: observed - {response.status_code}, expexted - {expected_code}.'
        return response
