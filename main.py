tasks = []
work_script = 1


def adding_task():
    task_name = input('Введите название задачи: ')
    task_description = input('Введите описание задачи: ')
    task = {
        "name": task_name,
        "description": task_description
    }
    tasks.append(task)
    print('Задача добавлена!')

    print("""
    1. Добавить еще задачу
    2. Вернутся в меню
    """)
    select_ = int(input('Введите номер нужного пункта: '))
    if select_ == 1:
        adding_task()


def list_tasks():
    for index in range(len(tasks)):
        print(f'{index}: Название: {tasks[index]["name"]} Описание: {tasks[index]["description"]}')

    return


def delete_task():
    for index in range(len(tasks)):
        print(f'{index}: {tasks[index]}')

    del_num = int(input('Введите номер задачи которую надо удалить: '))
    del tasks[del_num]

    print("""
    1. Удалить еще одну задачу
    2. Назад
    """)

    select_ = int(input('Введите номер нужного пункта: '))

    if select_ == 1:
        delete_task()
    elif select_ == 2:
        return


def completed_task():
    for index in range(len(tasks)):
        print(f'{index}: {tasks[index]}')

    select_ = int(input('Введите номер задачи: '))


def start_panel():
    while work_script == 1:
        print("""
        Функционал:

        1. Добавить задачу
        2. Список задач
        3. Редактирование задач
        4. Удалить задачу
        5. Отметить задачу как выполненную
        6. Выход""")

        select_variant = int(input('Введите номер нужного пункта: '))

        if select_variant == 1:
            adding_task()
        elif select_variant == 2:
            list_tasks()
        elif select_variant == 3:
            print(3)
            # edit_task()
        elif select_variant == 4:
            delete_task()
        elif select_variant == 5:
            completed_task()
        elif select_variant == 6:
            return


start_panel()
