#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
#  File Name        : pip-describe
#  Author           : E:V:A
#  Last Modified    : 2018-02-08
#  Version          : 1.0.1
#  License          : GPLv3
#  URL              : https://github.com/E3V3A/pip-date
# Description:      : Show full text package description from PyPI
#----------------------------------------------------------------------
# NOTE:  We don't do the summary as it is already available
#        from the `pip search` results.
#  [ ]   But we can always add CLI switch `-s` for summary
#----------------------------------------------------------------------
import os, sys
#import requests as req

try:
    import requests as req
# exception ImportError as err:     # 3.3
except ModuleNotFoundError as err:  # 3.6
    print("\nThis program need the \"requests\" package to work.")
    print("Please download and install from:\nhttps://github.com/requests/requests")
    print(err)
    sys.exit(1)

__version__ = '1.0.1'

def usage() :
    print("\n Usage:  %s <package-name>\n" % os.path.basename(__file__)) # sys.argv[0]
    print(" This will return the full-text package description (usually the README)")
    print(" as found on PyPI, for any given <package-name>.\n")
    print(" This script is part of the pip-date package at:")
    print(" https://github.com/E3V3A/pip-date/\n")
    sys.exit(2)

narg = len(sys.argv) - 1
if narg == 1:
    pkg = sys.argv[1]
else:
    usage()

url = 'https://pypi.org/pypi/%s/json' % pkg
res = req.get(url)
if res.status_code == 200:
    dat = res.json()
    #smm = dat['info']['summary'].strip()        # (short) description
    des = dat['info']['description'].strip()    # long_description (often full README)
    print("\nPackage Description:")
    print("-"*80)
    print("%s" % des)
    print("-"*80)
else:
    print('\nERROR (%s): Package \"%s\" doesn\'t exist!' % (res.status_code,pkg))
    sys.exit(2)

sys.exit(0)
