#!/bin/bash
python main.py
docker pull boardsource/bs-python
docker run -v $(pwd)/build_out:/build_out -v $(pwd)/cpy/circuitpython:/cpy/circuitpython boardsource/bs-python && bash post_build.sh