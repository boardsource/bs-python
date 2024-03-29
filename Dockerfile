FROM ubuntu:20.04

USER root
WORKDIR /cpy
COPY ./dockersetupcmd.sh .

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    # Development files
    build-essential \
    git \
    bzip2 \
    gcc-aarch64-linux-gnu\ 
    python3.8\
    python3-pip\
    gettext\
    curl\
    wget && \
    apt-get clean
    
RUN wget -qO- https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2019q4/gcc-arm-none-eabi-9-2019-q4-major-x86_64-linux.tar.bz2 | tar -xj
RUN apt-get update

# Get Rust
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y

RUN echo 'source $HOME/.cargo/env' >> $HOME/.bashrc



ENV PATH "/cpy/gcc-arm-none-eabi-9-2019-q4-major/bin:$PATH"
ENV PATH="/root/.cargo/bin:${PATH}"

RUN git config --global --add safe.directory /cpy/circuitpython
RUN git config --global --add safe.directory '*'



# RUN apt-get update && apt-get install -y gettext librsvg2-bin git mingw-w64 latexmk texlive-fonts-recommended texlive-latex-recommended texlive-latex-extra gcc-aarch64-linux-gnu wget python3.8 python3-pip && apt-get clean
# RUN make fetch-submodules
# RUN pip3 install -r requirements-dev.txt
# RUN pip3 install --upgrade click==7.1.2
# RUN make -C mpy-cross
CMD ["bash","dockersetupcmd.sh"]

# CMD ["sleep","3600"]
