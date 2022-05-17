##
# bs-python
#
# @version 0.4

CPYPREFIX := cpy/circuitpython
KMKPREFIX := kmk/kmk_firmware
THIS_DIR := $(dir $(abspath $(firstword $(MAKEFILE_LIST))))

.PHONY: default
default: run

.PHONY: all
all: init build

.PHONY: clean
clean:
	sudo rm -rf ${CPYPREFIX}
	sudo rm -rf ${KMKPREFIX}

J=1
.PHONY: run
run:
	clean
	python3 main.py $(J)
	docker pull boardsource/bs-python
	docker run -v ${THIS_DIR}cpy/circuitpython:/cpy/circuitpython boardsource/bs-python 
	bash post_build.sh

# end
