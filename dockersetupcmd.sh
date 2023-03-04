cd circuitpython
make fetch-submodules
pip3 install --upgrade -r requirements-dev.txt
make -C mpy-cross && bash dockerbuildcmd.sh