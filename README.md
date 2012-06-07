JadeLessCoffee Sublime Build
============================

JadeLessCoffee serves a very simple and single purpose: combine three rapid-development languages into one compiler. 
This is a sublime-build package to use JadeLessCoffee's compiler.

Important
---------

This uses the `make` system on Unix/Linux systems. It has not been tested on Windows.


Requirements
------------

**The JadeLessCoffee compiler** It will need to be installed. <http://github.com/Nuulogic/jadelesscoffee>

After installing node.js:
`$ sudo npm -g install https://github.com/Nuulogic/jadelesscoffee.git`


Installation
------------

Download the source as a zip or check it out. Either way copy the `JadeLessCoffee` folder to your Sublime Text 2 Packages folder:
OS X: `/Users/*username*/Library/Application\ Support/Sublime\ Text\ 2/Packages/`
Linux: `/home/*username*/.config/sublime_text/Packages/`
Windows: `\AppData\Roaming\Sublime Text 2\Packages\`

Usage
-----

Be sure to set the Build System to JadeLessCoffee: Tools -> Build System -> Export JadeLessCoffee

By default the builder looks for a `./src` folder and outputs to the base directory of the project.
It generates a `Makefile` or if a `Makefile` exists it makes a `jlc` target.

The JadeLessCoffee Sublime Build checks for certain types of projects.


Django
------

If **Django** is detected with the presence of:
* `./templates/`
* `./static/`
* `./manage.py`

These are used as the sources:
* ./templates/src 
* ./static/src


Helpful/Useful
--------------

Jade syntax highlighting
<https://github.com/miksago/jade-tmbundle>

HTML2Jade bin is helpful sometimes too
<https://github.com/donpark/html2jade>


LESS syntax highlighting
<https://github.com/creationix/LESS.tmbundle>


CoffeeScript syntax highlighting
<https://github.com/jashkenas/coffee-script-tmbundle>