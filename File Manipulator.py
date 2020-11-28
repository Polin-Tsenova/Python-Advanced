import os

while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-")
    action = tokens[0]
    file_name = tokens[1]
    if action == "Create":
        with open(file_name, 'w') as file:
            print()
    if action == "Add":
        content = tokens[2]
        with open(file_name, 'a') as file:
            file.write(content + "\n")
    if action == "Replace":
        old_string = tokens[2]
        new_string = tokens[3]
        try:
            text = ''
            with open(file_name, 'r') as file:
                text = file.read()
            text = text.replace(old_string, new_string)
            with open(file_name, 'w') as file:
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")
    if action == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")


