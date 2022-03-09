from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'OSC requests based query'
LONG_DESCRIPTION = 'Requests based interactions with the Open Source Context APIs'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="oscquery_req",
        version=VERSION,
        author="Open Source Context",
        author_email="<support@oscontext.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['requests'],

        keywords=['python', 'OSC', 'requests'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Information Security",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Linux :: Linux",
        ]
)
