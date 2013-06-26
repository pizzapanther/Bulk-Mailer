import sys

from setuptools import setup, find_packages

setup(
    name = "bulkmailer",
    version = '13.6.1',
    description = "API library for accessing GAE Bulk Mailer",
    url = "https://github.com/pizzapanther/Bulk-Mailer",
    author = "Paul Bailey",
    author_email = "paul.m.bailey@gmail.com",
    license = "BSD",
    packages = ['bulkmailer',],
    install_requires = [
      'requests==1.2.3',
    ],
)