from users.supervisor import Supervisor


# пример набора действий супервизора при разметке данных
def supervisor1():
    config = {
        'db_host': '',
        'db_port': '',
        'store_host': '',
        'store_port': '',
        'store_type': 'FTP',
        'user': '',
        'password': ''
    }
    visor = Supervisor(**config)
    paths = ['/home/amurashkin/1.txt', '/home/amurashkin/2.txt']
    # Набор изображений загрузить в глобальное хранилище.
    visor.send_files(paths)

    # Выбрать множество изображений.
    # Выбрать объекты, которые необходимо разметить на данном множестве.
    files = visor.get_store_by_filter({})
    ids = ['fa92130', 'ee3321f94d']
    # Назначить оператора для разметки некоторых объектов.
    operators = visor.get_operators()
    operator_id = 123
    visor.set_operator(operator_id, ids)

    result = visor.get_marked_files(ids)

    visor.set_correct_marked_file(ids[0])


def main():
    supervisor1()


if __name__ == "__main__":
    main()
