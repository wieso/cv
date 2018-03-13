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

        print(self.size)

    def __get_size_local_storage(self):
        size = 0
        for dirpath, dirnames, filenames in os.walk(self.path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                size += os.path.getsize(fp)
        return size

    # Синхронизация локального хранилища с глобальным
    def sync(self, gs: GlobalStorage, files_set: list):
        pass