import os

def find_and_replace_in_file(path,find,replace):
    with open(path, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace(find, replace)
    # print(filedata)
    with open(path, 'w') as file:
        file.write(filedata)
    print(f'replacing "{find}" with "{replace}" in {path}')

def supervisor_file():
    file_path = "./cpy/circuitpython/supervisor/supervisor.mk"
    find_and_replace_in_file(file_path,"CircuitPython","BsPython")
    find_and_replace_in_file(file_path,"circuitpython.org","github.com/boardsource/bs-python")
def filesystem_file():
    file_path = "./cpy/circuitpython/supervisor/shared/filesystem.c"
    find_and_replace_in_file(file_path,'"CIRCUITPY")','"BSPYTHON")')
    find_and_replace_in_file(file_path,"print(\"Hello World!\")\n","from kmk.json_keymap import JsonMap\nkeyboard = JsonMap(\"layout.json\").return_keyboard()\nif __name__ == \"__main__\":\n    keyboard.go()\n")
def do_all_the_changes():
    supervisor_file()
    filesystem_file()
