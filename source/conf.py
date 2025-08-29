# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'AERtronic_Lite'
copyright = '2025, Hammurabi Sierra'
author = 'Hammurabi Sierra'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "breathe",
]

breathe_projects = {
    "AERtronic_Lite": "C:/Users/Hammurabi.Sierra/Documents/GIT/AERtronic_Lite_2.0/ESP-IDF/Documentation/xml"
}

breathe_default_project = "AERtronic_Lite"

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
