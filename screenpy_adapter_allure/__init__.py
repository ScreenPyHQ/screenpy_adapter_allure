# -*- coding: utf-8 -*-

"""
                            ScreenPy Adapter: Allure
                                                                      FADE IN:
INT. SITEPACKAGES DIRECTORY

ScreenPy Adapter: Allure adds an Adapter for the Narrator's microphone, which
will send output to an Allure report.

:copyright: (c) 2022–2022 by Perry Goy.
:license: MIT, see LICENSE for more details.
"""


from .adapters import AllureAdapter

__all__ = [
    "AllureAdapter",
]
