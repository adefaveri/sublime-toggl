from base64 import b64encode
import json

from ..ssl import load_ssl
load_ssl()

from urllib.request import *


class TogglBaseApi():
    SESSION_URL = 'https://www.toggl.com/api/v8/sessions'
    SESSION_COOKIE_FROM_HEADER = 'Set-cookie'
    SESSION_COOKIE_TO_HEADER = 'Cookie'

    session_cookie = None

    def is_logged(self):
        return self.session_cookie is not None

    def authenticate(self, api_token):
        response = self.request(self.SESSION_URL, None, self.build_auth_header(api_token), 'POST')

        if response is False:
            self.session_cookie = None
            return
        else:
            self.session_cookie = response.getheader(self.SESSION_COOKIE_FROM_HEADER)

    def build_auth_header(self, api_token):
        phrase = api_token+':api_token'
        encoded_phrase = b64encode(phrase.encode())

        return {'Authorization': 'Basic '+encoded_phrase.decode()}

    def request(self, url, datas=None, headers={}, method='GET'):
        if self.is_logged():
            headers[self.SESSION_COOKIE_TO_HEADER] = self.session_cookie

        request = Request(url, datas, headers, None, False, method)
        response = urlopen(request)

        if response.status is not 200:
            return False
        else:
            return response

    def get_response(self, response):
        if response is False:
            return None
        else:
            return json.loads(response.read().decode())

    def prepare_datas(self, datas):
        return json.dumps(datas).encode('utf-8')
