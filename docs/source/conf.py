# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

# Ensure project root is importable so autodoc can import `ndustria`
sys.path.insert(0, os.path.abspath('../..'))

project = 'ndustria'
copyright = '2026, Mackenzie Ticoras'
author = 'Mackenzie Ticoras'
release = '2026.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
	'sphinx.ext.autodoc',
	'sphinx.ext.napoleon',
	'sphinx.ext.autosummary',
	'sphinx.ext.viewcode',
	'myst_parser',
	'sphinx_autodoc_typehints',
]

autosummary_generate = True

# Autodoc settings
autodoc_member_order = 'bysource'
autodoc_typehints = 'description'

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Keep the Read the Docs sidebar visible on every page
html_sidebars = {
	'**': [
		'about.html',
		'navigation.html',
		'relations.html',
		'searchbox.html',
	]
}

# Theme options to control sidebar behavior
html_theme_options = {
	'collapse_navigation': False,
	'sticky_navigation': True,
	# Increase navigation depth so deeper pages are visible (set to a suitable number)
	'navigation_depth': 4,
}
