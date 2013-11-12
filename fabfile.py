from fabric.api import *

env.hosts = ['www.pylit.org']

def build():
    """generate HTML docs"""
    local('sphinx-build -b html -d _build/doctrees . _build/html')

def pdf():
    """generate PDF docs"""
    local('sphinx-build -b latex -d _build/doctrees . _build/latex')
    with lcd('_build/latex'):
        local('pdflatex RRBweb.tex')

def new_project():
    """create new virtualenv for this projet"""
    local('rm -rf venv')
    local('virtualenv --no-site-packages venv')

def gen_style():
    """process sass files to css"""
    with lcd('code/app/static/css'):
        local('python -mscss < pylit.scss > pylit.css')

def push():
    """push local changes to GitHub"""
    msg = raw_input('Commit msg: ')
    local('git add --all .')
    local('git commit -m "%s"' % msg)
    local('git push origin master')

def deploy():
    """push code to github, then pull to ww.pylit.org"""
    with cd('RRBweb'):
        run('git pull')
