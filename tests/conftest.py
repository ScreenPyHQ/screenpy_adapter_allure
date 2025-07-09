from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple
from unittest import mock

import pytest
from allure_pytest.listener import AllureListener

if TYPE_CHECKING:
    from collections.abc import Generator


class AllureTrappings(NamedTuple):
    manager: mock.Mock
    listener: AllureListener
    logger: mock.Mock


@pytest.fixture(autouse=True)
def mock_allure_trappings() -> Generator:
    """Mock the Allure magic we're doing in the AllureAdapter."""
    plugin_manager_path = "screenpy_adapter_allure.adapters.plugin_manager"
    with mock.patch(plugin_manager_path) as mocked_manager:
        mocked_listener = mock.Mock(spec=AllureListener)
        mocked_logger = mock.Mock()
        mocked_listener.allure_logger = mocked_logger
        mocked_manager.get_plugins.return_value = [mocked_listener]

        yield AllureTrappings(mocked_manager, mocked_listener, mocked_logger)
