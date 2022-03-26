import os
import shutil

board_dir="./bs_python_boards"
cpy_dir = "./cpy/circuitpython/ports"
def move_boards():
    for subdir in os.listdir(board_dir):
        board_type = f'{board_dir}/{subdir}'
        for board in os.listdir(board_dir+"/"+subdir):
            board_dest =f'{cpy_dir}/{subdir}/boards/{board}' 
            board_src= f'{board_dir}/{subdir}/{board}'
            shutil.copytree(board_src, board_dest) 
            print(f'moving {board} from {board_src} to {board_dest}')

def generate_build_script():
    print("pass")