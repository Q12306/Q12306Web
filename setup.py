from setuptools import setup, find_packages
from os.path import join, isfile
from os import walk
import Q12306


def read_file(filename):
    with open(filename) as fp:
        return fp.read().strip()


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


def package_files(directories):
    paths = []
    for item in directories:
        if isfile(item):
            paths.append(join('..', item))
            continue
        for (path, directories, filenames) in walk(item):
            for filename in filenames:
                paths.append(join('..', path, filename))
    return paths


setup(
    name='Q12306',
    version=Q12306.version(),
    description='distributed crawler',
    keywords=['Q12306', 'scrapy', 'distributed'],
    author='germey',
    author_email='cqc@cuiqingcai.com',
    url='http://pypi.python.org/pypi/Q12306/',
    license='MIT',
    install_requires=read_requirements('requirements.txt'),
    packages=find_packages(),
    entry_points={
        'console_scripts': ['Q12306 = Q12306.cmd:cmd']
    },
    package_data={
        '': package_files([
            'Q12306/server/static',
            'Q12306/server/core/templates',
            'Q12306/templates',
            'Q12306/VERSION'
        ])
    },
    publish=[
        'sudo python3 setup.py bdist_egg',
        'sudo python3 setup.py sdist',
        'sudo python3 setup.py bdist_egg upload'
        'sudo python3 setup.py sdist upload'
    ]
)
