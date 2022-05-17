import json
import os
import cpy_git 
import board_mapping
import misc_file_changes
import build_from_json

def load_json(path,cpu_cores):
    cpy_git.git_checkout()
    f = open(path)
    data = json.load(f)
    board=data["board"]
    frozen_libs=data["frozen_libs"]
    default_files=data["default_files"]
    for file in default_files:
        file["data"]=open(file["content"]).read()
    dest_path=board_mapping.move_single_board(cpu_cores,board)
    board_mapping.generate_build_script()    
    misc_file_changes.do_all_the_changes()
    misc_file_changes.add_frozen_libs(f'{dest_path}/mpconfigboard.mk',frozen_libs)

    print(dest_path)
    