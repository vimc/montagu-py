import requests


class MontaguAPI:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        auth_url = self.build_url('authenticate/')
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(auth_url, data='grant_type=client_credentials', auth=(username, password),
                                 headers=headers)
        if response.status_code != 200:
            # TODO: throw error
            print("ERROR: " + str(response.status_code))
        self.token = response.json()['access_token']

    def build_url(self, route):
        return '{}/v1/{}'.format(self.base_url, route)
