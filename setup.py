
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
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
