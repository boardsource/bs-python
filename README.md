# BS-Python
What is this all about? So we wanted something like kmkPython But after talking with the kmk team and hearing the challenges we thought we would start fresh. So welcome to BS_Python (pun very much intended) our version of KMKPython.

So the main idea here and how we are doing this differently is we as you can see dont have circuit_python in here. What we do is we script everything. We start by cloning circuit_python > check out the right branch > make all the code changes > build the boards

Let me break down what's going on and how you can use this. I will start by going over the code flow then I will tell you what you need to edit (if you need to edit anything) and how you can help out

## Quick links
[current boards](supported_boards.md)



## **important**
All scripts are intended to be run from the root so

**dont** do this
```
cd scripts
bash start.sh
```
**do** do this
```
bash scripts/start.sh
```



## Code flow
* scipts/start.sh <- enetry point
    * calls main.py
        * main.py <- start of the code
            * cpy_git <- handles all things to do with git
                * clone the repo
                * add submodules
            * misc_file_changes <- change cpy code
            * board_mapping <- this moves BS_python boards into the right place in cpy
                * genarates the build script and post build script
        * pulls the docker container or uses the one you build (see below)
        * starts the new docker container
            * runs the dockersetupcmd.sh
                *  this sets up the cloned cpy repo for building
            * runs the genarated build script that builds all the BS_Python boards
        * runs the genarated post build script
            * this moves all of the built .u2f files into the ./build_out and renames them



## Misc things you can do
below are the other scripts you can run and what they do
* scripts/build.sh            
    * builds docker container
        * that way you only need docker and python you don't need to make sure you can compile cpy
    * tries to push it as well.
* scripts/clean.sh
    * removes old cpy clones and builds.
* scripts/bash-container.sh
    * this is mostly for debugging the docker container
    * it dumps you into bash on the container so you can see what's going on in there
* scripts/kill-all.sh
    * kills all docker containers running (look out)

Ok now that you have an idea on how this flows together lets go over some things you might do and how you would go about doing them.

## Freeze xyz lib into xyz board and let everyone download that
So you will want to copy that board from the cpy folder (run main.py to get that). Then make your changes to it and place that into the ./bs_python_boards folder. Now Its very important you place it in the correct folder. When you take it from the cpy repo if it is from ports/nrf it needs to go into the nrf folder. If the folder does not exist just make it but it NEEDS to be spelled the same.

## Freeze a lib that is not in CPY
To freeze  another library you can simply add it to the FROZEN_REPO_LIST in cpy_git.py

## other code changes
Above is all that I have implemented But if you want to make random changes to the CPY code base feel free to do so. A few things I would like to ask of you. Make sure that the entry for your code is in misc_file_changes.py (unless another file is better eg: git changes should be in cpy_git.py). And make sure you add something to this file letting others know how to do your cool new change.

## TODO / HELP WANTED / DISCLAMER
* typo / spelling
* let me know if I need to make any more changes to stay legal
* Add some boards
* turn all my sick bash scripts into a make file LOL
* freeze in kmk in some way. But I want it compiled to .mpy
* I am a super python noob I barely know how to setup a python project. This one was setup using pipenv and python 3.9.x we dont have a reqerments.txt I dont know how to make one or if we need one we do have a pipfile tho.
* github action to add all the .uf2s from ./build_out to git hub releases
* add colors to the logs (just the python parts)
* inject custom code into circuitpython/supervisor/shared/filesystem.c to change the drive name and default code after we are freezing in kmk we will be able to have a u2f that is for cornes and it comes typing and working perfectly







