import requests


class Query:
    def make_query(self, url, data=None, method='get'):
        if method.lower() == 'get':
            return requests.get(url, data=data)
        elif method == 'post':
            return requests.post(url, data=data)
