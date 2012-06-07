import os
from os import path

def is_project(project_path):
    
    #check for templates and static folder and manage.py. If they exists this is likely a django project.
    templates_folder = path.normpath(project_path + '/templates')
    static_folder = path.normpath(project_path + '/static')
    manage_file = path.normpath(project_path + '/manage.py')

    return path.exists(templates_folder) and path.exists(static_folder) and path.exists(manage_file)