import os
import re

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

def add_frozen_libs(mk_path,libs_to_add):
    with open(mk_path, 'r') as oldfile,open("temp.mk", 'w')as file :
        for line in oldfile:
            if 'FROZEN_MPY_DIRS' not in line:
                file.write(line)
    with open("temp.mk", 'r')as file:
        filedata = file.read()
    for lib in libs_to_add:
        filedata+=f'\nFROZEN_MPY_DIRS += $(TOP)/frozen/{lib}'
    with open(mk_path, 'w') as file:
        file.write(filedata)

# def make_default_file_func(file_name,file_data,index):
#     function_sig=f'static void make_sample_code_file_{index}(FATFS *fatfs)'+ "{"
#     function_body=f'#if CIRCUITPY_FULL_BUILD
#     FIL fs;
#     UINT char_written = 0;
#     const byte buffer[] = "{file_data}";
#     // Create or modify existing code.py file
#     f_open(fatfs, &fs, "/{file_name}", FA_WRITE | FA_CREATE_ALWAYS);
#     f_write(&fs, buffer, sizeof(buffer) - 1, &char_written);
#     f_close(&fs);
#     #else
#     make_empty_file(fatfs, "/{file_name}");
#     #endif
#     '+"}"
def add_default_files(default_files):
    file_path = "./cpy/circuitpython/supervisor/shared/filesystem.c"


def do_all_the_changes():
    supervisor_file()
