# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath("../"))

# -- Project information

project = 'PLCreX'
copyright = '2022, Marcel Werner'
author = 'Marcel Werner'

release = '0.2'
version = '0.2.x'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

