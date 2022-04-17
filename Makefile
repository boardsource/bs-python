##
# bs-python
#
# @version 0.4

CPYPREFIX := cpy/circuitpython
BUILDOUT := build_out

.PHONY: default
default: run

.PHONY: clean
clean:
	rm -rf ${CPYPREFIX}

.PHONY: run
run:
	python3 main.py
	docker pull boardsource/bs-python
	docker run -v ./${BUILDOUT}:/build_out -v ${CPYPREFIX}:/cpy/circuitpython boardsource/bs-python
	bash post_build.sh

# end
