##
# bs-python
#
# @version 0.4

CPYPREFIX := cpy/circuitpython

.PHONY: default
default: run

.PHONY: all
all: init build

.PHONY: clean
clean:
	rm -rf ${CPYPREFIX}

.PHONY: run
run:
	python3 main.py
	docker pull boardsource/bs-python
	docker run -v $(pwd)/build_out:/build_out -v $(pwd)/cpy/circuitpython:/cpy/circuitpython boardsource/bs-python && bash post_build.sh

# end
