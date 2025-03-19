import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'Drone Security Analyst'
copyright = '2024'
author = 'Your Name'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
