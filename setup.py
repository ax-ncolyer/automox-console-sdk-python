# coding: utf-8

"""
    Automox Console API

    API for use with the Automox Console  # noqa: E501

    OpenAPI spec version: 2021-09-01
    Contact: support@automox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "automox-console-sdk"
VERSION = "0.1.2"
DESCRIPTION = "Automox Console SDK for Python"

with open('README.md', 'r') as fh:
    long_description = fh.read()

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="support@automox.com",
    url="https://github.com/AutomoxCommunity/automox-console-sdk-python",
    keywords=["Swagger", "Automox Console API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9'
    ]
)
