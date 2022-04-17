import cpy_git 
import board_mapping
import misc_file_changes
import sys

def main(cpu_cores):
    cpy_git.git_checkout()
    misc_file_changes.do_all_the_changes()
    board_mapping.move_boards(cpu_cores)


if __name__ == '__main__': 
    cpu_cores=1
    if int(sys.argv[1])>1:
        cpu_cores=int(sys.argv[1])
    main(cpu_cores)