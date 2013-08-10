# -*- coding: utf-8 -*-
import sys, os
import cloud_sptheme as csp

# -- General configuration -----------------------------------------------------
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'ACC.webcore'
copyright = u'2013, Roie R. Black'

version = '0.1'
release = '0.1'

today_fmt = '%B %d, %Y'
exclude_patterns = ['_build']

pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------

html_theme = "cloud"
html_theme_path = [csp.get_theme_dir()]

html_title = "Base Website Docs"
html_short_title = "ACC.webcore"
html_logo = '_static/images/ACClogo.png'
html_static_path = ['_static']
html_last_updated_fmt = '%b %d, %Y'
html_use_index = True

html_show_sphinx = True
html_show_copyright = True

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
'papersize': 'letterpaper',
'pointsize': '12pt',
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'ACC.webcore.tex', u'Base Website Docs',
   u'Roie R. Black', 'manual'),
]

latex_logo = '_static/images/ACClogo.png'
