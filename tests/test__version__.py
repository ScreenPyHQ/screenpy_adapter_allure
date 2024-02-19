from __future__ import annotations

from screenpy_adapter_allure import __version__


def test_metadata() -> None:
    assert __version__.__title__ == "screenpy_adapter_allure"
    assert __version__.__license__ == "MIT"
    assert __version__.__author__ == "Perry Goy"
