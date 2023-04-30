import configparser

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


akarichan_config = Config()
