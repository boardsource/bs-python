import git
import subprocess
import shutil
PATH = "./cpy/circuitpython"
KMK_PATH = "./kmk/kmk_firmware"
PEGBOARDS_PATH="./pegboards/pegboards"
REPO_URL = "https://github.com/adafruit/circuitpython.git"
KMK_REPO_URL = "https://github.com/KMKfw/kmk_firmware"
PEGBOARDS_REPO_URL="git@github.com:daysgobye/pegBoards.git"
BRANCH = "7.2.x"
FROZEN_REPO_LIST = ["https://github.com/adafruit/Adafruit_CircuitPython_DisplayIO_SSD1306.git",
"https://github.com/adafruit/Adafruit_CircuitPython_SSD1306.git"]

def clean_dir():    
    try:
        shutil.rmtree(PATH)
    except OSError as e:
        print("Error: %s : %s" % (PATH, e.strerror))
def add_frozen_lib(repo):
    submodule_path= f'{PATH}/frozen'
    for lib_url in FROZEN_REPO_LIST:
        print(f'adding frozen lib from this url: {lib_url}')
        process  = subprocess.Popen(["git", "submodule", "add",lib_url],cwd=submodule_path)
        process.wait()

        # repo.git.submodule.add(submodule_path,lib_url)


def move_kmk():
    kmk_src= f'{KMK_PATH}/kmk'
    kmk_dest=f'{PATH}/frozen/kmk/kmk'
    shutil.copytree(kmk_src, kmk_dest) 

def git_checkout():
    clean_dir()
    repo = git.Repo.clone_from(REPO_URL, PATH)
    repo.git.checkout(BRANCH)
    # pegboards_repo = git.Repo.clone_from(PEGBOARDS_REPO_URL, PEGBOARDS_PATH)
    kmk_repo = git.Repo.clone_from(KMK_REPO_URL, KMK_PATH)
    add_frozen_lib(repo)
    move_kmk()