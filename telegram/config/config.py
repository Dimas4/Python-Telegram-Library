import pathlib
import yaml


class Config:
    def __init__(self):
        self._config = self.parse_config()
        self.api_methods = self._config['api']

    @staticmethod
    def parse_config():
        path = pathlib.Path(__file__).parent / 'config.yaml'
        with open(path, 'r') as file:
            data = yaml.load(file)
        return data
