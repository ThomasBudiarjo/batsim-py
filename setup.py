from setuptools import setup
from os import path


def read_requirements_file(filename):
    file = '%s/%s' % (path.dirname(path.realpath(__file__)), filename)
    with open(file) as f:
        return [line.strip() for line in f]


setup(
    name='batsim_py',
    author='lccasagrande',
    version='0.1',
    python_requires='>=3.7',
    install_requires=read_requirements_file('requirements.txt'),
)
