import os

from storages.globalstorage import GlobalStorage

B = 1
KB = 1024
MB = KB * 1024
GB = MB * 1024


class LocalStorage:
    SIZE_STORAGE = 20 * GB

    def __init__(self, path='/tmp/cv/local'):
        self.path = path

        if os.path.exists(path):
            self.size = self.__get_size_local_storage()
        else:
            os.makedirs(path, mode=0o777, exist_ok=False)
            self.size = 0

    def __get_size_local_storage(self):
        size = 0
        for dirpath, dirnames, filenames in os.walk(self.path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                size += os.path.getsize(fp)
        return size

    # Получить список хэшей, которые есть локально
    def __get_all_hashes(self) -> set:
        return {str(i) for i in range(0, 20, 2)}

    # Синхронизация локального хранилища с глобальным
    # files_set - файлы, которые необходимо синхронизировать, остальные можно удалять
    def sync(self, gs: GlobalStorage, files_set: list):
        local_files = self.__get_all_hashes()
        remote_files = set(files_set)

        # Те файлы, которых нет в локальном хранилище
        only_remote_files = remote_files.difference(local_files)

        # Те файлы, которые можно удалить
        may_delete_files =  local_files.difference(remote_files)

        print('Файлы в глобальном хранилище ', remote_files)
        print('Файлы в локальном хранилище ', local_files)
        print('Файлы, которые необходимо скачать ', only_remote_files)
        print('Файлы, которые можно удалить ', may_delete_files)
