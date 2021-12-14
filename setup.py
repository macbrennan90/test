
from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'basic package'

# Setting up
setup(
    name="test-package-macb",
    version=VERSION,
    author="Mac Brennan",
    author_email="<mac.brennan.90@gmail.com>",
    description=DESCRIPTION,
    packages=['hello'],
    package_dir={'': 'src'}
    install_requires=[]
)
