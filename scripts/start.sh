#!/bin/bash
python main.py
docker pull boardsource/bs-python
docker run -v $(pwd)/cpy/circuitpython:/cpy/circuitpython boardsource/bs-python && bash post_build.sh