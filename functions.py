FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write to-do items list to a text file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


# This piece of code will only run if this file itself is ran as main (directly ran)
# otherwise, if being imported do not execute this portion
if __name__ == "__main__":
    print("Hello from functions")
