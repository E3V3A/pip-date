### pip-date - Date your pip packages!

[![pypi supported versions][1]][2]
[![PyPI version][3]][4]
[![Maintenance][5]][6]
[![GitHub last commit][7]][8]
[![Average time to resolve an issue][9]][10]

[1]: https://img.shields.io/pypi/pyversions/pip-date.svg
[2]: https://pypi.python.org/pypi/pip-date
[3]: https://badge.fury.io/py/pip-date.svg
[4]: https://badge.fury.io/py/pip-date
[5]: https://img.shields.io/badge/Maintained%3F-yes-green.svg
[6]: https://GitHub.com/E3V3A/pip-date/graphs/commit-activity
[7]: https://img.shields.io/github/last-commit/E3V3A/pip-date.svg
[8]: https://github.com/E3V3A/pip-date/commits/master "Last commits to Master branch"
[9]: http://isitmaintained.com/badge/resolution/E3V3A/pip-date.svg
[10]: http://isitmaintained.com//project/E3V3A/pip-date "Average time to resolve an issue"

A simple *Python3* CLI tool to show the installation or modification times of all your pip packages.

| STATUS: | Version | Date | Maintained? |
|:------- |:------- |:---- |:----------- |
| Working | `1.0.2` | 2018-12-02 | YES |

---

Example Output:

![Full](./docs/screen1.png)

![Full](./docs/screen2.png)

---

**Q:** *What does **`pip-date`** do?*

The primary use is for finding the *time* when a certain pip package was last modified or installed. 
It is basically using one or more of: **atime, ctime** and **mtime** from the file status (*stat*) info.
This is essentially equivalent to using the \*nix *stat* command, but is handled differently on Windows. 
(See below for further details.)

Using this information, it can show you and highlight packages that may have been corrupted or outdated. 
I also has some functionality of checking packages for outdated and deprecated installation methods. 

But it can do more. Some features are:

- Highlight packages with inconsistent file modification times (*mTime*).
- Highlight package **versions** which are not conforming to the [PEM-0440](https://www.python.org/dev/peps/pep-0440/) standard.
- Highlight packages installed with an unusual package distribution *priority* given by:  **`[chk, src, bin, egg, dev]`**
- Highlight *`setuptools`* dependency packages for easy review
- Show package installation type:  with pip/wheel as **`wheel`**, and source as **`sdist`**  (**FIX!**)
- Show package installation location:   **`usr`** for `--user` and **`sys`** for *global* installations.
- Show correct file modification time, depending on OS/FS architecture (*mtime* vs *ctime*)

**Q:** *What does it **not** do?*

- Does not install packages
- Does not show dependencies
- Does not (yet) show packages in a *`virtualenv`* or *`pipenv`* envrionment (**ToDo**)
- Does not check package consistency 
- Does not show the very first time you installed a package, if it has been updated since.  
  (Althought there are left-over artifacts that may show otherwise, we don't look for these.)


**Q:** *Why is this needed?*

It probably isn't, **BUT**...

Because python packages often rely on a large number of sub-dependencies, it is very easy to accidentally 
overwrite some required dependency of one package with a different version needed by another package. 
You will never know about it, until it breaks something. One common scenario causing package corruption 
is that you have installed some package XXX using pip, but then get an OS update and install the update 
using you OS packagemanagement system, like `apt-get install XXX`, which would probably overwrite the 
*globally* installed pip package. This is especially true for beginners of python, who has not yet learned 
how to use a virtual environment, and installing evything in either the global system (default) or 
user (`--user`) environments. This may also occur when installing packages from sources, or when 
you have to run some other non-pip installers like `setup.py`, `make install` or like, 
and you don't really know what it is going to do. 


**Q:** *What else is included?*

* A script called **`pip-describe`**, that will do what *pip* doesn't, which is to show 
the full text package description from PyPI, for a given *package*. Usually the README.

* A script called **`pipbyday`**, that will print a simple table with:  
  `mTime/aTime` +  `package-name` + `package-version`, sorted by time.

* A script called **`pyfileinfo`**, that will show detailed file and date information 
for a given file using python's `os.stat` info.

* A script called **`pyOSinfo`**, that will print a number of *os, system* 
and *platform* variables, as seen by your Python interpreter.


**Q:** *Will I continue to support this tool?*

Sure, if it is broken, but I will not spend any more time for new features. So if you would like to add 
something just send me a PR, or at the very least, a detailed code snippet of what I need to implement.

---

### Dependencies


* [requests](https://github.com/requests/requests) - used by `pip-describe` to get PyPI info

and what you already have: 
* [Python3](https://www.python.org/) 
* [pip](https://github.com/pypa/pip/).


### Installation 

There is nothing to install really. Just download the `pip-date.py` file and make sure to place it in your `PATH`.

**For pip installation:**

```bash
pip install pip-date
```


**For single file installation:**

```bash
cd /usr/bin/
wget https://github.com/E3V3A/pip-date/raw/master/pip-date
chmod 755 pip-date
```


**For developer installation:**

```bash
git clone https://github.com/E3V3A/pip-date.git
cd pip-date
pip install pip-date --user
```


### How to Run

```bash
pip-date      # When it's in your PATH
./pip-date    # When it's not in your PATH
```

---

### References:

**Time Stamps**

It's quite amusing to see how different OS's and File System's (FS) are handling file time stamps.
In the Linux world the available time stamps are called [atime](), [ctime]() and [mtime](), where 
they are generally available through the *`stat`* command. However, Windows systems doesn't have 
this commmand because they are using a different way to *blah blah*... 

To summarize the issue of finding the *`"last modification time"`* (*mtime*) when using Python on a 
Windows architechture, we need to use *`ctime`* instead. Thus we use `platform.architecture()` to 
check the machine's *(bits, linkage)* tuple for the "WindowsPE" string, and blatantly assuming
that it has a Windows FS that need *ctime*, and that anything else should use *mtime*. 

Then we use: `os.path.getctime(pkg_loc)` to get the file time stamp.

For all the gory details, see: 
[here](https://linuxhandbook.com/file-timestamps/), 
[here](https://www.unixtutorial.org/atime-ctime-mtime-in-unix-filesystems/) and 
[here](https://en.wikipedia.org/wiki/MAC_times). 

---

#### Glossary:

* **`bdist`** - *"Built Distribution"*:  
	A Distribution format containing files and metadata that only need 
    to be moved to the correct location on the target system, to be 
    installed. *Wheel* is such a format, whereas distutil’s *Source 
    Distribution* is not, in that it requires a build step before it 
	can be installed. (A **"Binary Distribution"** is also a *bdist*, but 
	with additional compiled extensions.)

* **`sdist`** - *"Source Distribution"*:  
    A distribution format (usually generated using python setup.py 
    sdist) that provides metadata and the essential source files needed 
    for installing by a tool like pip, or for generating a Built 
    Distribution.

* **`egg`** - **[deprecated]**:  
    The older *Built Distribution* format introduced by *setuptools*, 
	which is being replaced by *wheel*.

* **`wheel`** - "":  
    A *Built Distribution* **format** introduced by [**`PEP-0427`**](https://www.python.org/dev/peps/pep-0427/), which is 
	intended to replace the "egg" format. A wheel (`bdist_wheel`) is a 
	ZIP-format archive with a specially formatted file name and using 
	the **`.whl`** extension. Normally, you need one wheel file for each 
	operating system and architechture. And that list can get long for big 
	projects, like *numpy*.


---

#### Recommeded Similar Tools:

- **[pip-check](https://github.com/bartTC/pip-check/)** - Check you pip package update status with nice ANSI colored CLI
- **[pip-chill](https://github.com/rbanffy/pip-chill)** - Lists only the dependencies (or not) of installed packages

---

#### Bugs and Warnings

None


#### ToDo / Help Needed

See issues marked [ToDo](https://github.com/E3V3A/pip-date/issues?q=is%3Aopen+is%3Aissue+label%3AToDo).

#### Contribution

Feel free to post issues and PR's related to this tool.  
Feel free to fork, break, fix and contribute. Enjoy!


#### Additional Badges

[![build status][11]][12] [![Codacy Badge][13]][14] [![codecov][15]][16]

---

#### License

[![GitHub license][21]][22]  
A license to :sparkling_heart:!

<sub>I use `GPLv3` because sharing code modifications is more beneficial for the world.</sub>

[11]: https://ci.appveyor.com/api/projects/status/github/pip-date/pip-date?branch=master&svg=true
[12]: https://ci.appveyor.com/project/pip-date/pip-date
[13]: https://api.codacy.com/project/badge/Grade/176ceaabe43d4113b535f2fbd0487a9e
[14]: https://www.codacy.com/app/E3V3A/pip-date?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=E3V3A/pip-date&amp;utm_campaign=Badge_Grade
[15]: https://codecov.io/gh/pip-date/pip-date/branch/master/graph/badge.svg
[16]: https://codecov.io/gh/pip-date/pip-date

[21]: https://img.shields.io/github/license/E3V3A/pip-date.svg
[22]: https://github.com/E3V3A/pip-date/blob/master/LICENSE.txt