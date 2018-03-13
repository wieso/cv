from users.user import User


class Supervisor(User):
    """
    Отправка файлов в глобальное хранилище
    
    :param files - список путей до файлов
    :return hashes - список уникальных id файлов
    """

    def send_files(self, files: list) -> list:
        hashes = self.gs.load_files(files)
        return hashes

    """
    Получение информации о файлах из базы со всей необходимой информацией, фильтрацией по разным параметрам
    id файла
    id оператора, который будет или уже разметил файл
    статус (в работе, размечен, подтвержден супервизором)
    """

    def get_store_by_filter(self, filters: dict) -> dict:
        data = self.ms.get_files(filters)
        return data

    """
    Получение списка операторов, для которых будет назначаться работа
    """

    def get_operators(self) -> dict:
        data = self.ms.get_operators()
        return data

    """
    Для набора изображений назначаем оператора, который будет их размечать
    """

    def set_operator(self, operator_id: int, img_hashes: list):
        pass

    """
    Получение размеченного изображения. Самого файла, мета данных и данных разметки.
    """

    def get_marked_files(self, img_hashes: list):
        return {}

    """
    Отметка корректной разметки изображения
    """

    def set_correct_marked_file(self, img_hash: str):
        pass