from storages.globalstorage import GlobalStorage
from storages.metastorage import MetaStorage
from storages.localstorage import LocalStorage


class User:
    def __init__(self,
                 db_host: str = '',
                 db_port: int = '',
                 store_host: str = '',
                 store_port: int = '',
                 store_type: str = 'FTP',
                 local_path: str = '/tmp/cv/local',
                 user: str = '',
                 password: str = ''
                 ):
        self.user = user
        self.password = password

        # Подключение к глобальному хранилищу
        gs = GlobalStorage(store_host, store_port, store_type, user, password)
        self.gs = gs.connect()

        # Подключение к базе (серверу), где хранится вся информация о разметке,
        # мета информация, информация об операторах и т.п.
        ms = MetaStorage(db_host, db_port, user, password)
        self.ms = ms.connect()

        # Получение информации об авторизованном пользователе
        self.uid = self.ms.who()['uid']

        self.ls = LocalStorage(local_path)
