#!/usr/bin/env python
import os

from pkg_resources import resource_filename
from setuptools import setup, find_packages

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_version():
    # depending on your execution context the version file
    # may be located in a different place!
    vsn_path = resource_filename(__name__, 'hvac/version')
    if not os.path.exists(vsn_path):
        vsn_path = resource_filename(__name__, 'version')
        if not os.path.exists(vsn_path):
            raise Exception("%s is missing" % vsn_path)

    with open(vsn_path, 'r') as fh:
        version = fh.read()

    return version


def load_long_description():
    readme_path = os.path.join(BASE_DIR, 'README.md')
    with open(readme_path, 'r') as fh:
        long_description = fh.read()
    return long_description


def get_extra_require():
    extra_require = {
        'parser': []
    }
    for extra_require_key in extra_require.keys():
        requirements_file = 'requirements-{suffix}.txt'.format(suffix=extra_require_key)
        requirements_path = os.path.join(BASE_DIR, requirements_file)
        with open(requirements_path, 'r') as fh:
            # drop any comments; either full line comments or comments following the requirement line
            requirements = [l.split()[0] for l in fh.readlines() if not l.startswith('#')]
            extra_require[extra_require_key] = requirements

    return extra_require


setup(
    name='hvac',
    version=get_version(),
    description='HashiCorp Vault API client',
    long_description=load_long_description(),
    long_description_content_type="text/markdown",
    author='Ian Unruh <ianunruh@gmail.com>, Jeffrey Hogan <jeff.hogan1@gmail.com>',
    author_email='admin@hvac.network',
    url='https://github.com/hvac/hvac',
    keywords=['hashicorp', 'vault'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    packages=find_packages(),
    install_requires=[
        'requests>=2.7.0',
    ],
    include_package_data=True,
    package_data={'hvac': ['version']},
    extras_require=get_extra_require(),
)
