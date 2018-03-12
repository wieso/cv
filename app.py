class GlobalStore:
    def __init__(self, store_host: str, store_port: int, store_type: str = 'FTP',
                 user: str = '', password: str = ''):
        self.user = user
        self.password = password

        # Подключение к глобальному файловому хранилищу
        self.store_host = store_host
        self.store_port = store_port
        self.store_type = store_type

    def load_files(self, files: list) -> list:
        return []


class Supervisor:
    def __init__(self, db_host: str = '', db_port: int = '', store_host: str = '', store_port: int = '',
                 store_type: str = 'FTP', user: str = '', password: str = ''):
        self.user = user
        self.password = password

        # Подключение к глобальному файловому хранилищу
        self.store_host = store_host
        self.store_port = store_port
        self.store_type = store_type

        # Подключение к базе (серверу), где хранится вся информация о разметке, мета информация и т.п.
        self.db_host = db_host
        self.db_port = db_port

    '''
    Отправка файлов в глобальное хранилище
    '''

    def send_files(self, files: list) -> list:
        gs = GlobalStore(self.store_host, self.store_port, self.store_type, self.user, self.password)
        hashes = gs.load_files(files)
        return hashes

    '''
    Получение списка файлов из глобального хранилища со всей необходимой информацией
    id файла
    id оператора, который будет или уже разметил файл
    статус (в работе, размечен, подтвержден супервизором)
    '''

    def get_store(self):
        return {}

    '''
    Получение списка операторов, для которых будет назначаться работа
    '''

    def get_operators(self):
        return {}

    '''
    Для набора изображений назначаем оператора, который будет их размечать
    '''

    def set_operator(self, operator_id: int, img_hashes: list):
        pass

    '''
    Получение размеченного изображения. Самого файла, мета данных и данных разметки.
    '''

    def get_marked_files(self, img_hashes: list):
        return {}

    '''
    Отметка корректной разметки изображения
    '''

    def set_correct_marked_file(self, img_hash: str):
        pass


def main():
    visor = Supervisor()
    paths = ['/home/amurashkin/1.txt', '/home/amurashkin/2.txt']
    # Набор изображений загрузить в глобальное хранилище.
    visor.send_files(paths)

    # Выбрать множество изображений.
    # Выбрать объекты, которые необходимо разметить на данном множестве.
    files = visor.get_store()
    ids = ['fa92130', 'ee3321f94d']
    # Назначить оператора для разметки некоторых объектов.
    operators = visor.get_operators()
    operator_id = 123
    visor.set_operator(operator_id, ids)

    result = visor.get_marked_files(ids)

    visor.set_correct_marked_file(ids[0])


if __name__ == "__main__":
    main()
