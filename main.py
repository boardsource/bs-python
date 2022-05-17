import cpy_git 
import board_mapping
import misc_file_changes
import build_from_json
import sys


def main(cpu_cores):
    cpy_git.git_checkout()
    misc_file_changes.do_all_the_changes()
    board_mapping.move_boards(cpu_cores)


if __name__ == '__main__': 
    cpu_cores=1
    json_path=None
    try:
        if int(sys.argv[1])>1:
            cpu_cores=int(sys.argv[1])
            if "json" in sys.argv[2]:
                json_path=sys.argv[2]
        elif "json" in sys.argv[1]:
            json_path=sys.argv[1]    
    except:    
        print("no cpu cores given using default")   
    print(json_path)
    if json_path is None:
        main(cpu_cores)
    else:
        build_from_json.load_json(json_path,cpu_cores)
  