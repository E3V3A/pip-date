#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
#  File Name        : pip-search.py
#  Author           : E:V:A
#  Last Modified    : 2022-01-23
#  Version          : 1.0.2
#  License          : GPLv3
#  URL              : https://github.com/E3V3A/pip-date
#  Description      : Getting a list of pip packages matching a string
# 
#  References: 
#   [1] https://docs.python.org/3/howto/regex.html
#	[2] https://github.com/victorgarric/pip_search
#	[3] 
#
#----------------------------------------------------------------------
# ToDo:
#	[ ] Add color
#	[ ] Add '-n <n>' comand line switch to show max (max_shown) matches. 
#	[ ] Put result list in local file under $USERPROFILE (Win) or $HOME (*nix)
#	[ ]	In windows search type: "manage app execution aliases"
#----------------------------------------------------------------------
# 
# Getting a list of pip packages
#	curl -i -X OPTIONS -H 'Accept: application/json' -H "Content-Type: application/json" https://pypi.org/simple/ >pypilist.html
#	cat pypilist.html | grep -io '<a href=".*">' | sed 's/\(<a href="\|\">\)//g' >plink.txt
#	sed -e 's/^\/simple\///' |sed -e 's/.$//'
#----------------------------------------------------------------------
#
#	python -c "a='ars*'; print('yes') if('*' in a) else print('no');"
#	if ('*' in arg):
#		rep = r'{}'.format(arg)
#	else: 
#		rep = r'.*{}.*'.format(arg)
#----------------------------------------------------------------------
import os, re, sys
import datetime
import requests
from lxml import html

__author__ = "E:V:A (E3V3A)"
__copyright__ = "GPLv3 2022"
__version__ = '1.0.2'

debug = 0
showline = '  '+'-'*60

#TS = '{:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())
TS = '{:%Y%m%d}'.format(datetime.datetime.now())
filename = 'tmp_piplist_{}.txt'.format(TS)

name_list = []
match_list = []
my_headers = {'user-agent': 'curl/7.55.1','accept': 'application/json', 'content-type': 'application/json', 'referer': 'https://pypi.org/', 'cache-control': 'no-cache', 'connection': 'close'}

#----------------------------------------------------------
# Print Usage
#----------------------------------------------------------
def usage():
    print('\n Usage:  {} <partial-name> | "<RegEx>"\n'.format( os.path.basename(__file__)) )
    print(' Getting a list of pip packages matching a partial name string.')
    print(' The string can also be a RegEx for matching unknown packages.')
    print(' This script is part of the \'pip-date\' package.')
    print(" Please file any bug reports at:")
    print(" https://github.com/E3V3A/pip-date/\n")
    print(' Version:  {}'.format(__version__))
    print(' License:  {}\n'.format(__copyright__))
    sys.exit(2)

#----------------------------------------------------------
# CLI arguments
#----------------------------------------------------------
arg  = "pyt"
narg = len(sys.argv) - 1
if narg != 1:
	usage()
arg = sys.argv[1] 				# CLI provided search string (args[0])

rep = r'.*{}.*'.format(arg)		# pattern
rec = re.compile(rep, re.I)		# compiled

#----------------------------------------------------------------------
# Utilitiy Functions
#----------------------------------------------------------------------

def print_warn():
    print('\n  Warning!')
    print('  Searching all ~350,000 pip packages can take a very long time!')
    print('  This script will first download the 19 MB (HTML) file, and only')
    print('  then search the list for the content requested.')
    print('  This can take up to 20 seconds.\n')

def save_list(file, data):
	print('  Saving package list to file:\n  ./{} '.format(file))
	if os.path.exists(file):
		print('  WARNING:  The file already exists, so skipping.')
	else: 
		f = open(file, 'w')
		for i in data:
			f.write('{}\n'.format(i))
		f.close()

def load_list(file):
	data = []
	print('  Trying to load package list from file...',end='')
	if os.path.exists(file):
		f = open(file, 'r')
		#with open(file, 'r') as f:
		for x in f:
			item = x[:-1]
			data.append(item)
		f.close()
		print('ok\n  ./{}'.format(file))
	else: 
		print('FAIL\n  Previous package list file is too old or doesn\'t exist!')
		#print('  (./{})'.format(file))
	if (debug): print('\nDATA:\n{}\n...\n{}\n\n'.format(data[0:20], data[len(data)-100:]))
	return data

def download_pip_list():
	name_list = []
	#name_list = ''
	print('\n  Downloading full pip list... ', end='')
	with requests.Session() as s:
		try:
			r = s.get('https://pypi.org/simple/', headers=my_headers)
		except:
			pass
	print('ok')

	tree = html.fromstring(r.content)									# Use lxml to get package names	
	package_list = [package for package in tree.xpath('.//a/@href')]	# Grab the <a href="..."> part
	#print(showline)
	print('  Found {:,} packages in current list.\n'.format(len(package_list)))
	
	if (debug): print(package_list[1:30])

	p = re.compile(r'/simple/(.*)/')									# Only get the pip package name
	#name_list = list(filter(p.match, package_list))					# Maybe try using "filter" to match
	for i in package_list:
		item = p.match(i)
		name_list.append(item.group(1))
	
	if (debug): 
		print('  Package name list is now clean, with {:,} items.\n'.format(len(name_list)))
		print('\nDATA:\n{}\n...\n{}\n\n'.format(name_list[0:20], name_list[len(name_list)-100:]))
	return name_list

def print_matches(name_list):
	# Print matching package items
	j=0
	for i in name_list:
		m = rec.search(i)
		if not (m == None): 
			#print(m[0])
			match_list.append(m[0])
			j += 1

	#print(showline)
	print('\n  Found {:,} matches in current list.'.format(j))
	if (j >= 60): 
		print('\n  Only showing first 60 matches of list.')	# ToDo: .format(max_shown))
		print('  Try to narrow your search or use regex.')
		print(showline)
		#print(match_list[1:60])
		for x in match_list[1:60]: print('  {}'.format(x));
	else:
		print(showline)
		#print(match_list)
		for x in match_list: print('  {}'.format(x));
	print(showline)
	#print('\n')

#----------------------------------------------------------------------
#  Main
#----------------------------------------------------------------------

print_warn()

name_list = load_list(filename)
if not (name_list): 
	name_list = download_pip_list()
	save_list(filename, name_list)

print_matches(name_list)
print('ok\n')


#----------------------------------------------------------------------
#  EOF
#----------------------------------------------------------------------
