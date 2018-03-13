class GlobalStorage:
    gs = None

    def __init__(self, store_host: str, store_port: int, store_type: str = 'FTP',
                 user: str = '', password: str = ''):
        self.user = user
        self.password = password

        self.store_host = store_host
        self.store_port = store_port
        self.store_type = store_type

    # Реализуем подключение
    def connect(self):
        if self.gs is None:
            self.gs = self._connect()
        return self.gs

    def _connect(self) -> object:
        return self

    # Загрузить файлы в глобальное хранилище
    def load_files(self, files: list) -> list:
        return []

