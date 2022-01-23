#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pipbyday - Prints when python packages were installed
#----------------------------------------------------------------------
#  File Name        : pipbyday
#  Author           : E:V:A
#  Last Modified    : 2018-02-08
#  Version          : 1.0.1
#  License          : GPLv3
#  URL              : https://github.com/E3V3A/pip-date
#  Description      : Print a sorted list when python packages were installed
#                   : This is based on mtime or ctime, depending on OS
#----------------------------------------------------------------------

from __future__ import print_function
from datetime import datetime
import os, platform
import pkg_resources as p
from time import strftime

__version__ = '1.0.1'

if __name__ == "__main__":
    packages = []

    if platform.architecture()[1] == "WindowsPE":
        isWinFS = True
        print("\nUsing ctime for WindowsPE\n")
    else:
        isWinFS = False
        print("\nUsing mtime for Linux FS\n")

    # The package: "name version"
    for package in p.working_set:
        pkg_nam_ver = str(package)

        try:
            module_dir = next(package._get_metadata('top_level.txt'))
            pkg_loc = os.path.join(package.location, module_dir)
            os.stat(pkg_loc)

        except (StopIteration, OSError):
            try:
                pkg_loc = os.path.join(package.location, package.key)
                os.stat(pkg_loc)
            except:
                pkg_loc = package.location

        # aTime = access time ...
        # mtime = modification time
        # ctime = creation time BUT is the "real" last modification time on windows.
        if isWinFS:
            mtime = os.path.getctime(pkg_loc)   # modification time on Windows
        else:
            mtime = os.path.getmtime(pkg_loc)   # modification time on Linux

        mtime = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d  %H:%M:%S")
        #packages.append([mtime, pkg_nam_ver])
        packages.append([mtime, pkg_nam_ver, pkg_loc])

    for mtime, pkg_nam_ver, pkg_loc in sorted(packages):
        print("{:22} : {:<30} : {:<40}".format(mtime.ljust(22,' '), pkg_nam_ver, pkg_loc))
    #for mtime, pkg_nam_ver in sorted(packages):
    #    print("{:22} : {:<30}".format(mtime.ljust(22,' '), pkg_nam_ver))

print("\nDone!")
