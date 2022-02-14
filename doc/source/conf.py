"""Configuration file for shared.docs.pyansys.com landing page."""
from datetime import datetime

from pyansys_sphinx_theme import pyansys_logo_black

project = 'pyansys.shared'
copyright = f"(c) {datetime.now().year} ANSYS, Inc. All rights reserved"
author = 'ANSYS Inc.'
html_title = f"PyAnsys Shared Components"

release = version = '1.1.0'

# use the default pyansys logo
html_logo = pyansys_logo_black
html_theme = 'pyansys_sphinx_theme'

html_theme_options = {
    "github_url": "https://github.com/pyansys/",
    "show_prev_next": False,
    "show_breadcrumbs": True,
    "additional_breadcrumbs": [("PyAnsys Documentation", "https://docs.pyansys.com")]
}

intersphinx_mapping = {
    'openapi-common': ('https://openapi.docs.pyansys.com/', None)
}

# Sphinx extensions
extensions = ["sphinx.ext.intersphinx"]

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'
