from telegram.exception.exception import BadRequestError
from telegram.config.config import Config
from telegram.query.query import Query


class Bot:
    def __init__(self, token):
        self._token = token
        self._query = Query()
        self._config = Config()
        self._api_config = self._config.api_methods
        self._message_offset = 0

    def _generate_url(self, method, **kwargs):
        return self._api_config[method].format(**kwargs)

    def _make_query_get_key(self, url, data=None):
        data = self._query.make_query(url, data).json()
        if not data.get('result'):
            raise BadRequestError(data)
        return data['result']

    def get_last_message(self):
        messages = self.get_unread_messages()
        return None if len(messages) < 1 else messages[-1]

    def get_unread_messages(self, data=None):
        url = self._generate_url('get_unread_messages', token=self._token)
        data = self._make_query_get_key(url, data)
        messages = data[self._message_offset:]
        self._message_offset = len(data)
        return messages

    def send_message(self, chat_id, text):
        url = self._generate_url('send_message', token=self._token,  chat_id=chat_id, text=text)
        return self._make_query_get_key(url)
