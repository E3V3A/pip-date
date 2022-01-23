#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pyOSinfo - Show what Python thinks about your system environment
#----------------------------------------------------------------------
#   File Name       : pyOSinfo
#   Author          : E:V:A
#   Date            : 2018-02-08
#   Last Modified   : 2022-01-23
#   Version         : 1.0.2
#   License         : GPLv3
#   URL             : https://github.com/E3V3A/pip-date/
#   Description     : Show some system, os and platform information as seen by python3
#----------------------------------------------------------------------
# NOTE:
#   On Cygwin, yuo have to pay attention to the parts of the PATH
#   that is cpoied fromt he Windows (System PATH). This will interfere
#   with the resulsts of 'os.name' [nt vs posix], depeding on which
#   python*.exe was used. Try to test with:
#   ls -al `which python.exe`
#----------------------------------------------------------------------
import os, sys, platform, site
from os.path import join

__version__ = '1.0.2'

TRUECOLOR = "\x1b[38;2;255;100;0mTRUECOLOR\x1b[0m"

def hasUname():
    try:
        os.uname()[0]
        return True
    except:
        return False

print("\nCurrent OS variables as seen by Python3 (%s)\n" % platform.python_version() )
print('os.getenv(\"TERM\"):   %s' % os.getenv("TERM"))   # [xterm, xterm-color, xterm-256color]
print('os.name:             %s' % os.name )              # [posix, nt, java]
print('os.sys.platform:     %s' % os.sys.platform )      # [linux, win32, cygwin, darwin]
print('sys.platform:        %s' % sys.platform )         # [linux, win32, cygwin, darwin]
print('TRUECOLOR (orange):  %s' % TRUECOLOR )            # TRUECOLOR written in nice orange

# Apparently some Windows Pythons doesn't provide os.uname attribute.
# Like:  Winpython64-3.6.7.0Zero
print('\nos.uname:') # sysname, nodename, release, version, machine
if hasUname():
    print('\tnodename:      %s' % os.uname()[1] )   #
    print('\tmachine:       %s' % os.uname()[4] )   #
    print('\tsysname:       %s' % os.uname()[0] )   #
    print('\trelease:       %s' % os.uname()[2] )   #
    print('\tversion:       %s' % os.uname()[3] )   #
else:
    print('\tN/A' )

print('\nplatform:')
print('\tnode        :     %s' % platform.node() )
print('\tmachine     :     %s' % platform.machine() )
print('\tprocessor   :     %s' % platform.processor() )
print('\tsystem      :     %s' % platform.system() )
print('\trelease     :     %s' % platform.release() )
print('\tversion     :     %s' % platform.version() )
print('\tplatform    :     %s' % platform.platform() )
print('\tuname (6)   : {}'.format(platform.uname()) )                   # (system, node, release, version, machine) # not processor
print('\tarchitecture (2):  (%s,%s)' % platform.architecture() )        # (bits, linkage)
#print('\twin32_ver (4):     (%s,%s,%s,%s)' % platform.win32_ver() )    # (release, version, csd, ptype)

print("\nsite:")
print("\tgetusersitepackages: %s" % site.getusersitepackages())
i=0
for ploc in site.getsitepackages():                     # Returns a []
    print("\tgetsitepackages[%i]:  %s" % (i, ploc))     # site.getsitepackages()[0])
    i+=1
print()
print("\tPREFIXES (2) :        %s" % site.PREFIXES)
print("\tUSER_SITE    :        %s" % site.USER_SITE)
print("\tUSER_BASE    :        %s" % site.USER_BASE) 

print('\nsys.path:\n\t%s\n' % ('\n\t'.join(sys.path)) )

sys.exit(0)
