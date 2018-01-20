from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(
    name = "PyCryptax",
    version = "1.0.0",
    description = \
        "UK Income and Capital Gains Tax Calculator for Cryptocurrencies",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    author = "Matthew Mitchell",
    author_email = "pycryptax@thelibertyportal.com",
    url = "https://github.com/MatthewLM/PyCryptax",
    packages = ["pycryptax"],
    license = "MIT",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Topic :: Office/Business :: Financial :: Accounting",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Environment :: Console"
    ],
    entry_points = {
        "console_scripts" : ["pycryptax = pycryptax.__main__:main"]
    }
)

