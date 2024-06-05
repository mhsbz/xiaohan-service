from typing import Dict, Any

import yaml


class AppConfig:
    debug = True
    app_id = ""
    app_secret = ""
    app_token = ""

    def __init__(self, config_data: Dict[str, Any]):
        try:
            self.app_id = config_data["APP_ID"]
            self.app_token = config_data["APP_TOKEN"]
            self.app_secret = config_data["APP_SECRET"]
        except KeyError as e:
            raise KeyError(e)


with open('./app/configs/config.yaml', 'r') as stream:
    config_data = yaml.safe_load(stream)

app_config = AppConfig(config_data)
