FROM python:3

# apt update
RUN apt-get update
RUN apt-get install -y sudo

# add sudo user
RUN groupadd -g 1000 developer && \
    useradd  -g      developer -G sudo -m -s /bin/bash docker && \
    echo 'docker:docker' | chpasswd

RUN echo 'Defaults visiblepw'             >> /etc/sudoers
RUN echo 'docker ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER docker

RUN sudo apt-get update
ENV DEBIAN_FRONTEND noninteractive
RUN sudo apt-get -y install locales && \
    sudo localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
