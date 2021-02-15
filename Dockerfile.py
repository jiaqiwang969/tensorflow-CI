#!/usr/bin/env python
import codecs
import os
import shutil

from jinja2 import Environment, FileSystemLoader

source_root = os.path.split(os.path.abspath(__file__))[0]
env = Environment(loader=FileSystemLoader(source_root))
template = env.get_template('Dockerfile.template')

python_versions = [
    ('py2', '2.7'),
    ('py3', '3.6'),
]
tensorflow_versions = [
    ('tf1.5', '1.5.0'),
    ('tf1.11', '1.11.0'),
    ('tf1.12', '1.12.0'),
]

valid_names = set()
for pytag, pyver in python_versions:
    for tftag, tfver in tensorflow_versions:
        name = pytag + tftag
        valid_names.add(name)
        dir_name = os.path.join(source_root, name)
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        with codecs.open(os.path.join(dir_name, 'Dockerfile'), 'wb', 'utf-8') as f:
            cnt = template.render(
                python_version=pyver,
                tensorflow_version=tfver.replace('-', '')
            )
            f.write(cnt + '\n')

for name in os.listdir(source_root):
    dir_name = os.path.join(source_root, name)
    docker_file = os.path.join(dir_name, 'Dockerfile')
    if os.path.isfile(docker_file) and name not in valid_names:
        shutil.rmtree(dir_name)
