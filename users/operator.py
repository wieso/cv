from users.user import User
from storages.storage import StorageException


class Operator(User):
    # def __init__(self,
    #              db_host: str = '',
    #              db_port: int = '',
    #              store_host: str = '',
    #              store_port: int = '',
    #              store_type: str = 'FTP',
    #              local_path: str = '/tmp/cv/local/',
    #              user: str = '',
    #              password: str = ''):
    #     User.__init__(self, db_host, db_port, store_host, store_port, store_type, local_path, user, password)

    # Запуск синхронизации локального и глобального хранилищ для выполнения разметки
    def update_state(self):
        try:
            # Получить список неразмеченных файлов для текущего оператора
            files = map(lambda x: x.id, self.ms.get_files({'operator_id': self.uid, 'status': 'not marked'}))
            self.ls.sync(self.gs, files)
            return True
        except StorageException:
            return False
