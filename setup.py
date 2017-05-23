#!/usr/bin/env python

from os.path import dirname, join
import crisscross

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

curdir = dirname(__file__)
packages = [
    'crisscross',
    'crisscross.facades',
    'crisscross.platforms',
    'crisscross.platforms.linux',
    'crisscross.platforms.android',
    'crisscross.platforms.win',
    'crisscross.platforms.win.libs',
    'crisscross.platforms.ios',
    'crisscross.platforms.macosx',
    'crisscross.platforms.macosx.libs',
]

with open(join(curdir, "README.md")) as fd:
    readme = fd.read()

setup(
    name='crisscross',
    version=crisscross.__version__,
    description='Cross platform python wrapper for platform dependent features',
    long_description=readme,
    author='Bhavesh Anand',
    author_email='bhaveshanand7@gmail.com',
    packages=packages,
    package_data={'': ['LICENSE', 'README.md']},
    package_dir={'crisscross': 'crisscross'},
    include_package_data=True,
    license=open(join(curdir, 'LICENSE')).read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: None',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
