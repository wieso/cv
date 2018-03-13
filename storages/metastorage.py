class MetaStorage:
    ms = None

    def __init__(self, store_host: str, store_port: int, user: str = '', password: str = ''):
        self.user = user
        self.password = password
        self.store_host = store_host
        self.store_port = store_port

    def connect(self):
        if self.ms is None:
            self.ms = self._connect()
        return self.ms

    def _connect(self) -> object:
        return self

    # Получить информацию о файлах, удовлетворяющих заданным фильтрам
    def get_files(self, filters: dict) -> dict:
        return {}

    # Получить список операторов
    def get_operators(self) -> dict:
        return {}

    # Установить какой оператор размечает какие данные
    def set_operator(self, operator_id: int, img_hashes: list) -> bool:
        return True
