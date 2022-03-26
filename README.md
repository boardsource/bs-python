# bs-python
What is this all about? So we we wanted something like kmkPython But after talking with the kmk team and hearing the challanges we thought we would start fresh. So welcome to BS_Python (pun very much intended) our version of KMKPython.

So the main idea here and how we are doing this defferently is we as you can see dont have circuit_python in here. What we do is we script everything. We start by cloning circuit_python > check out the right branch > make all the code changes > build the boards

Let me break down whats going on and how you can use this. I will start by going over the code flow then I will tell you what you need to edit (if you need to edit anything) and how you can help out

## Code flow
* scipts/build.sh <- enetry point
    * calls main.py
        * main.py <- start of the code
            * cpy_git <- handles all things to do with git
                * clone the repo
                * add submodules
            * misc_file_changes <- change cpy code 
            * board_mapping <- this moves BS_python boards into the right place in cpy
    * builds docker container
        * that way you only need docker and python you dont need to make sure you can compile cpy
* scripts/start.sh
    * starts the newly built docker container and builds all of the BS_python boards

Ok now that you have an idea on how this flows together lets go over some things you might do and how you would go about doing them.

## Freez xyz lib into xyz board and let everyone download that
So you will want to copy that board from the cpy folder (run main.py to get that). Then make your changes to it and place that into the ./bs_python_boards folder. Now Its very important you place it in the correct foleder. When you take it from the cpy repo if it is from ports/nrf it needs to go into the nrf folder. If the folder does not exsist just make it but it NEEDS to be spelled the same.

## Freez a lib that is not in CPY
To freez a another libary you can simply add it to the FROZEN_REPO_LIST in cpy_git.py 

## other code changes
Above is all that I have implmented But if you want to make random changes to the CPY code base feel free to do so. A few things I would like to ask of you. Make sure that the entry for your code is in misc_file_changes.py (unless another file is better eg: git changes should be in cpy_git.py). And make sure you add somthing to this file letting other know how to do your cool new change.

## TODO / HELP WANTED / DISCLAMER

* Add some boards
* freez in kmk in some way. But I want it compiled to .mpy
* I am a super python noob I barly know how to setup a python project. This one was setup using pipenv and python 3.9.x we dont have a reqerments.txt I dont know how to make one or if we need one we do have a pipfile tho. 





