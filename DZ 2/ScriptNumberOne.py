HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запращиваем у пользователя).
show - напечатать все добавленные задачи.
"""

tasks = []
run = True

while run:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print(tasks)
    elif command == "add":
        task = input("Введите название задачи: ")
        tasks.append(task)
        print("Задача добавлена.")
    elif command == "exit":
        break
    else:
        print("Неизвестная команда")


print("Спасибо за использование! До свидания!")