# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'COmanage Registry User Guide'
copyright = '2026, The COmanage Project'
author = 'The COmanage Project'

# The short X.Y version and full release version.
# RTD manages version/release display via git branches and tags;
# these values appear in the built HTML as a fallback.
version = '5'
release = '5'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autosectionlabel',  # Auto-generate section labels for cross-refs
    'sphinx_design',                 # Card grids, badges, tabs, dropdowns
]

templates_path = ['_templates']

# Patterns relative to source directory to exclude from build
# Getting Started lessons that are drafted but not yet verified on Registry
# v5.2.0. Listed files are left out of the build (and so out of Read the
# Docs). To publish a lesson, delete its line here and add it to its module's
# toctree.
UNVERIFIED = [
    'getting-started/structure/first-co.rst',
    'getting-started/connections/source-hr-file.rst',
    # 'getting-started/connections/source-hr-api.rst',
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store'] + UNVERIFIED

# Warn on broken cross-references
nitpicky = False

# Prefix autosectionlabel targets with the document name to avoid collisions
autosectionlabel_prefix_document = True

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

html_theme_options = {
    'logo_only': False,
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
    'style_external_links': True,
}

# Site-wide metadata
html_title = 'COmanage Registry User Guide'
html_short_title = 'Registry User Guide'

# -- Extension configuration -------------------------------------------------

# sphinx_design: no additional config required for basic use
