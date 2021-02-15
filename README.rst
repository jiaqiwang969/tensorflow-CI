Docker Images for Running Tests with TensorFlow on Travis CI
============================================================

.. image:: https://travis-ci.org/haowen-xu/travis-tensorflow-docker.svg?branch=master
    :target: https://travis-ci.org/haowen-xu/travis-tensorflow-docker

This is a Ubuntu Docker image for running tests with various versions of Python and TensorFlow on `Travis CI <https://travis-ci.org>`_.

Versions
--------

Built versions are:

* Ubuntu 16.04 + Python 2.7 / 3.5 + TensorFlow 1.3 ~ 1.8
* Ubuntu 18.04 + Python 2.7 / 3.6 + TensorFlow 1.9 ~ 1.12

All the available tags can be retrieved at `Docker Hub <https://hub.docker.com/r/haowenxu/travis-tensorflow-docker/tags/>`_.

Usage
-----

An example `.travis.yml`::

    sudo: required
    services:
      - docker
    env:
      matrix:
      - PYTHON_VERSION=2 TENSORFLOW_VERSION=1.2
      - PYTHON_VERSION=3 TENSORFLOW_VERSION=1.2
      - PYTHON_VERSION=2 TENSORFLOW_VERSION=1.8
      - PYTHON_VERSION=3 TENSORFLOW_VERSION=1.8
    install:
      - docker pull "haowenxu/travis-tensorflow-docker:py${PYTHON_VERSION}tf${TENSORFLOW_VERSION}"
    script:
      - docker run
          -v "$(pwd)":"$(pwd)"
          -w "$(pwd)"
          -e TRAVIS="${TRAVIS}"
          -e TRAVIS_JOB_ID="${TRAVIS_JOB_ID}"
          -e TRAVIS_BRANCH="${TRAVIS_BRANCH}"
          "haowenxu/travis-tensorflow-docker:py${PYTHON_VERSION}tf${TENSORFLOW_VERSION}"
          bash -c "pip install -r requirements.txt && coverage run -m py.test && coveralls"

Development
-----------

To populate the Dockerfiles, execute the following command::

    pip install jinja2
    python Dockerfile.py

Local Build
-----------

::

    # to build a certain variant, for example, py3tf1.4
    docker build \
        --build-arg UBUNTU_MIRROR=archive.ubuntu.com \
        --build-arg CACHEBUST="$(date +%s)" \
        -t haowenxu/travis-tensorflow-docker:py3tf1.4 \
        py3tf1.4
