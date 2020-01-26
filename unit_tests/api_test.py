import unittest
from modules.api_base import ApiBase


class ApiBaseUnittest(unittest.TestCase):
    api = ApiBase()
    json_payload = "This is expected to be sent back as part of response body."

    def test_get_request(self):
        self.api.set_url("https://postman-echo.com/get?foo1=bar1&foo2=bar2")
        self.api.get()

        self.assertEqual(self.api.get_status_code(), 200)

    def test_post_request(self):
        self.api.set_url("https://postman-echo.com/post")
        self.api.post(self.json_payload)

        self.assertEqual(self.api.get_status_code(), 200)

        data_response_text = str(self.api.get_body()["data"].strip("\""))
        self.assertEqual(self.json_payload, data_response_text)

    def test_put_request(self):
        self.api.set_url("https://postman-echo.com/put")
        self.api.put(self.json_payload)

        self.assertEqual(self.api.get_status_code(), 200)

        data_response_text = str(self.api.get_body()["data"].strip("\""))
        self.assertEqual(self.json_payload, data_response_text)

    def test_delete_request(self):
        self.api.set_url("https://postman-echo.com/delete")
        self.api.delete(self.json_payload)

        self.assertEqual(self.api.get_status_code(), 200)

        data_response_text = str(self.api.get_body()["data"].strip("\""))
        self.assertEqual(self.json_payload, data_response_text)


if __name__ == '__main__':
    unittest.main()
