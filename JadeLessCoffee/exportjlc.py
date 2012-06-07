#!/usr/bin/env python

import os
from os import path

from subprocess import call, Popen, PIPE
import sys
import imp
import pkgutil
import re

project_path = path.abspath(sys.argv[1])
package_path = path.abspath(sys.argv[2])


# HOW THIS WORKS

current_type = 'default'
project_types = [name for _, name, _ in pkgutil.iter_modules(['projects'])]

for project_type in project_types:
    mod_file, mod_path, mod_desc = imp.find_module(project_type, ['projects'])
    if mod_file:
        mod = imp.load_module(project_type, mod_file, mod_path, mod_desc)
        try:
            if mod.is_project(project_path):
                current_type = project_type
                break
        except Exception as err:
            continue

makefile_path = path.normpath(project_path + '/Makefile') 
#read in the Makefile for this type
type_makefile_path = path.normpath('%s/projects/Makefile-%s' % (package_path, current_type))
if path.exists(type_makefile_path):
    type_makefile = open(type_makefile_path).read()
else:
    type_makefile = open(path.normpath('%s/projects/Makefile-%s' % (package_path, 'default'))).read()


if path.exists(makefile_path):
    #check for the jlc target
    makefile = open(makefile_path).read()
    jlc_regex = re.compile('^(\s*)jlc:$', re.MULTILINE)
    make_match = jlc_regex.search(makefile)
    if make_match is None:
        open(makefile_path, 'a').write('\n\n' + type_makefile)
else:
    open(makefile_path, 'w').write('\n' + type_makefile)

nodedenv = os.environ.copy()
nodedenv['PATH'] = '/usr/local/bin:' + nodedenv['PATH']
process = Popen(['make jlc'], cwd=project_path, shell=True, stdout=PIPE, stderr=PIPE, env=nodedenv)
(out, error) = process.communicate()
print(out)
print(error)
