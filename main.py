import cpy_git 
import board_mapping
import misc_file_changes

def main():
    cpy_git.git_checkout()
    misc_file_changes.do_all_the_changes()
    board_mapping.move_boards()


if __name__ == '__main__': 
    main()