"""
ScreenPy Adapter: Allure
"""

# (the ascii art would be too long for this one :( )

import importlib.metadata

metadata = importlib.metadata.metadata("screenpy_adapter_allure")

__title__ = metadata["Name"]
__description__ = metadata["Summary"]
__url__ = metadata["Home-page"]
__version__ = metadata["Version"]
__author__ = metadata["Author"]
__author_email__ = metadata["Author-email"]
__license__ = metadata["License"]
__copyright__ = f"2019-2024 {__author__}"
