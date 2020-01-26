import json
import requests


class ApiBase(object):
    response = None
    url = None

    def __init__(self):
        self.headers = {"Content-Type": "application/json"}

    def get(self, ssl_certificate=None):
        """
        GET request.
        :param ssl_certificate: To verify the SSL certification for Https endpoints
        :return: Response body
        """

        if ssl_certificate is None:
            ssl_certificate = False

        try:
            self.response = requests.get(self.url,
                                         headers=self.headers, verify=ssl_certificate)
            print("RESPONSE: {}".format(self.get_body()))
        except requests.exceptions.RequestException as e:
            print("Request could not be completed... {}".format(e))
        return json.loads(self.response.content)

    def post(self, payload=None):
        """
        POST request.

        :param payload: payload of the request
        :return: None
        """

        if payload is not None and self.headers['Content-Type'] == "application/json":
            payload = json.dumps(payload)

            try:
                self.response = requests.post(self.url, payload, headers=self.headers)
            except requests.exceptions.RequestException as e:
                print("Request could not be completed... {}".format(e))

    def put(self, payload=None, ssl_certificate=None):
        """
        PUT request.

        :param payload: payload of the request
        :param ssl_certificate: To verify the SSL certification for Https endpoints
        :return: None
        """

        if payload is not None and self.headers['Content-Type'] == "application/json":
            payload = json.dumps(payload)

        if ssl_certificate is None:
            ssl_certificate = False

        try:
            self.response = requests.put(self.url, payload, headers=self.headers, verify=ssl_certificate)
        except requests.exceptions.RequestException as e:
            print("Request could not be completed... {}".format(e))

    def delete(self, payload=None, ssl_certificate=None):
        """
        Delete request.

        :param payload: payload of the request
        :param ssl_certificate: To verify the SSL certification for Https endpoints
        :return: None
        """

        if ssl_certificate is None:
            ssl_certificate = False

        payload = json.dumps(payload)

        try:
            self.response = requests.delete(self.url, data=payload, headers=self.headers, verify=ssl_certificate)

        except requests.exceptions.RequestException as e:
            print("Request could not be completed... {}".format(e))

    def get_status_code(self):
        return self.response.status_code

    def get_body(self):
        return json.loads(self.response.text)

    def set_url(self, url):
        self.url = url
        """
        Add another header to the dictionary of headers

        :param key: Key
        :param value: Value
        """

    def add_to_header(self, key, value):
        self.headers[key] = value

    def delete_header(self, key):
        """
        Delete header from the dictionary of headers

        :param key: Key
        """

        try:
            del self.headers[key]
        except TypeError:
            print("Header {} is not available".format(key))
