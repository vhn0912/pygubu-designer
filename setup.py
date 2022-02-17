#!/usr/bin/env python3
# encoding: UTF-8

"""Build tar.gz for pygubu

Needed packages to run (using Debian/Ubuntu package names):

    python3-tk
"""
from __future__ import print_function

import os
import platform
from io import open

import pygubudesigner

VERSION = pygubudesigner.__version__

_dirname_ = os.path.dirname(__file__)

readme_path = os.path.join(_dirname_, 'README.md')
product_txt_path = os.path.join(_dirname_, 'requirements', 'product.txt')

try:
    from setuptools import setup
    from setuptools.command.install import install
except ImportError:
    from distutils.command.install import install
    from distutils.core import setup


class CustomInstall(install):
    """Custom installation class on package files.
    """

    def run(self):
        """Run parent install, and then save the install dir in the script."""
        install.run(self)

        #
        # Remove old pygubu.py from scripts path if exists
        spath = os.path.join(self.install_scripts, 'pygubu')
        for ext in ('.py', '.pyw'):
            filename = spath + ext
            if os.path.exists(filename):
                os.remove(filename)
        #
        # Remove old pygubu-designer.bat
        if platform.system() == 'Windows':
            spath = os.path.join(self.install_scripts, 'pygubu-designer.bat')
            if os.path.exists(spath):
                os.remove(spath)


def get_requirements():
    requirements = [
        i.strip('\n') for i in open(product_txt_path, 'r').readlines()
        if not i.startswith('#') and len(i.strip()) > 0
    ]
    return requirements


setup(
    name='pygubu-designer',
    version=VERSION,
    license='GPL-3',
    author='Alejandro Autalán',
    author_email='alejandroautalan@gmail.com',
    description='A tkinter GUI builder.',
    long_description=open(readme_path, 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/alejandroautalan/pygubu-designer',

    packages=['pygubudesigner', 'pygubudesigner.util',
              'pygubudesigner.widgets', 'pygubudesigner.preview'],
    package_data={
        'pygubudesigner': [
            'images/images-gif/*.gif',
            'images/images-gif/widgets/*/*.gif',
            'images/images-png/*.png',
            'images/images-png/widgets/*/*.png',
            'ui/*.ui',
            'locale/*/*/*.mo',
            'template/*.mako',
        ],
    },
    entry_points={
        'gui_scripts': [
            'pygubu-designer = pygubudesigner.main:start_pygubu',
        ]
    },
    cmdclass={
        'install': CustomInstall,
    },
    install_requires=get_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Software Development :: User Interfaces",
    ],
    python_requires=">=3.6",
)
