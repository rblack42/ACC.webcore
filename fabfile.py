from fabric.api import *

def build():
    """generate HTML docs"""
    local('sphinx-build -b html -d build/doctrees . build/html')

def new_project():
    """create new virtualenv for this projet"""
    local('rm -rf venv')
    local('virtualenv --no-site-packages venv')

def gen_style():
    """process sass files to css"""
    with lcd('code/app/static/css'):
        local('python -mscss < pylit.scss > pylit.css')
