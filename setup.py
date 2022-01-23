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
    version          = '1.0.4',
    author           = 'E:V:A',
    author_email     = 'xdae3v3a@gmail.com',
    description      = 'Show the installation/modification times of all your pip packages and other tools',
    #long_description = 'A light CLI tool-set to show the installation or modification times of all your pip packages.',
    #long_description_content_type='text/plain',
    long_description = readme(),
    long_description_content_type = 'text/markdown',
    license='LICENSE.txt',
    url = 'https://github.com/E3V3A/pip-date/',
    packages = find_packages(),
    scripts=['pip-date', 'pip-describe', 'pip-search.py', 'pipbyday', 'pyfileinfo', 'pyOSinfo'],
    keywords = 'pip date package management setuptools wheel egg stat os',
    install_requires=[
        'requests', 'lxml',
    ],
    python_requires = '>=3',
    classifiers=[
        #'Private :: Do Not Upload',
        'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Version Control',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Software Distribution',
		'Topic :: System :: Systems Administration',
    ],
    project_urls={
        'Bug Reports': 'https://github.com/E3V3A/pip-date/issues',
        #'Funding' : 'https://donate.pypi.org',
        #'Credits' : 'http://saythanks.io/to/example',
        #'Source'  : 'https://github.com/pypa/sampleproject/',
    },
    #zip_safe = False,
)
