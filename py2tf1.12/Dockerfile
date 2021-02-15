FROM ubuntu:18.04

MAINTAINER Haowen Xu <haowen.xu@outlook.com>

ARG UBUNTU_MIRROR=archive.ubuntu.com
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV PATH="${PATH}"
ENV SHELL=/bin/bash


RUN sed -i "s/archive.ubuntu.com/${UBUNTU_MIRROR}/g" /etc/apt/sources.list && \
    DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y dist-upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends apt-utils && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        wget \
        git \
        locales \
        language-pack-en \
        python python-dev python-pip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    python -m pip install --upgrade pip setuptools && \
    python -m pip install --upgrade numpy coverage mock pytest sphinx matplotlib pillow "coveralls>=1.1" && \
    python -m pip install "ipython[all]<6" && \
    python -m pip install tensorflow==1.12.0

CMD ["/bin/bash"]
