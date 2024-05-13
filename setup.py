#!/usr/bin/env python3

import setuptools

install_requires = [
    "argparse"
]

setuptools.setup(
    name="pidcat3",
    version="1.0",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'pidcat = pidcat:run',
        ],
    },
    include_package_data=True,
)