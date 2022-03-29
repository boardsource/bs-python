import os
import shutil

board_dir="./bs_python_boards"
cpy_dir = "./cpy/circuitpython"
build_script= "#!/bin/bash\n"
post_build_script= "#!/bin/bash\n"
def generate_build_script():
    build_script_path= f'{cpy_dir}/dockerbuildcmd.sh'
    with open(build_script_path, 'w') as file:
        file.write(build_script)
    with open("./post_build.sh", 'w') as file:
        file.write(post_build_script)
    print(f'making build script in "{build_script_path}"')

def add_board_to_build_script_board(board,board_dir):
    global build_script
    global post_build_script
    build_script+=f'cd ports/{board_dir}\n'
    build_script+=f'make BOARD={board}\n'
    build_script+=f'sleep 100\n'
    build_script+=f'cd ../..\n'
    post_build_script+=f'cp ./cpy/circuitpython/ports/{board_dir}/build-{board}/firmware.uf2 ./build_out/{board}.uf2\n'

def move_boards():
    for subdir in os.listdir(board_dir):
        board_type = f'{board_dir}/{subdir}'
        for board in os.listdir(board_dir+"/"+subdir):
            board_dest =f'{cpy_dir}/ports/{subdir}/boards/{board}' 
            board_src= f'{board_dir}/{subdir}/{board}'
            shutil.copytree(board_src, board_dest) 
            print(f'moving {board} from {board_src} to {board_dest}')
            add_board_to_build_script_board(board,subdir)
    generate_build_script()