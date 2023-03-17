import os

def find_and_replace_in_file(path,find,replace):
    with open(path, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace(find, replace)
    # print(filedata)
    with open(path, 'w') as file:
        file.write(filedata)
    print(f'replacing "{find}" with "{replace}" in {path}')

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def supervisor_file():
    file_path = "./cpy/circuitpython/supervisor/supervisor.mk"
    find_and_replace_in_file(file_path,"CircuitPython","BsPython")
    find_and_replace_in_file(file_path,"circuitpython.org","github.com/boardsource/bs-python")
def filesystem_file():
    file_path = "./cpy/circuitpython/supervisor/shared/filesystem.c"
    find_and_replace_in_file(file_path,'"CIRCUITPY")','"BSPYTHON")')
    find_and_replace_in_file(file_path,'const byte buffer[] = "print(\\"Hello World!\\")\\n";','const byte buffer[] = "from kmk.json_keymap import JsonMap\\nkeyboard = JsonMap(\\"layout.json\\").return_keyboard()\\nif __name__ == \\"__main__\\":\\n    keyboard.go()\\n";')
    find_and_replace_in_file(file_path,'// Create or modify existing code.py file','const byte buffer2[] = "from kmk.json_boot import JsonBoot\\nboot = JsonBoot(\\"layout.json\\")\\n";\n    f_open(fatfs, &fs, "/boot.py", FA_WRITE | FA_CREATE_ALWAYS);\n    f_write(&fs, buffer2, sizeof(buffer2) - 1, &char_written);\n    f_close(&fs);\n')
def do_all_the_changes():
    supervisor_file()
    filesystem_file()
