from setuptools import setup, find_packages
from os import path

#------------------------------------------------------------------------------
# The current standard for setup info.
# For details, see:
#  https://packaging.python.org/guides/distributing-packages-using-setuptools/
#  https://github.com/pypa/sampleproject/blob/master/setup.py
#  https://pypi.org/classifiers/
#  https://choosealicense.com/
#------------------------------------------------------------------------------

def readme():
    # Get the long description from the README file
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        return f.read()

setup(
    name             = 'pip-date',
    version          = '1.0.1',
    author           = 'E:V:A',
    author_email     = 'xdae3v3a@gmail.com',
    description      = 'Show the installation/modification times of all your pip packages',
    long_description = 'A simple Python3 CLI tool to show the installation or modification times of all your pip packages.',
    long_description_content_type='text/plain',
    #long_description = readme(),
    #long_description_content_type = 'text/markdown',
    license='LICENSE.txt',
    url = 'https://github.com/e3v3a/pip-date/',
    packages = find_packages(),
    #scripts=['pip-date/pip-date', 'pip-date/pipbyday'],
    scripts=['pip-date', 'pipbyday'],
    keywords = 'pip date package setuptools wheel egg',
    python_requires = '>=3',
    classifiers=[
        #'Private :: Do Not Upload',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Version Control',
        'Topic :: System :: Software Distribution',
        'Topic :: System :: Installation/Setup',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/e3v3a/pip-date/issues',
        #'Funding' : 'https://donate.pypi.org',
        #'Credits' : 'http://saythanks.io/to/example',
        #'Source'  : 'https://github.com/pypa/sampleproject/',
    },
    #zip_safe = False,
)
