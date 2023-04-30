import configparser
import json

class Config:
    def __init__(self) -> None:
        self._config = configparser.ConfigParser()
        self._config.read('./config.ini')
    
    @property
    def token(self) -> str:
        token = self._config.get('BOT', 'token')
        if len(token) == 0:
            raise Exception('tokenが設定されていません。config.iniを見直してください')
        return token
    
    @property
    def guild_ids(self) -> list[int]:
        guild_ids: str = self._config.get('BOT', 'guild_ids')
        return json.loads(guild_ids)


akarichan_config = Config()
