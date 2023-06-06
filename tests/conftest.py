from collections import namedtuple
from typing import Generator
from unittest import mock

import pytest
from allure_pytest.listener import AllureListener

AllureTrappings = namedtuple("AllureTrappings", "manager listener logger")


@pytest.fixture(autouse=True, scope="function")
def mock_allure_trappings() -> Generator:
    """Mock the Allure magic we're doing in the AllureAdapter."""
    plugin_manager_path = "screenpy_adapter_allure.adapters.plugin_manager"
    with mock.patch(plugin_manager_path) as mocked_manager:
        mocked_listener = mock.Mock(spec=AllureListener)
        mocked_logger = mock.Mock()
        mocked_listener.allure_logger = mocked_logger
        mocked_manager.get_plugins.return_value = [mocked_listener]

        yield AllureTrappings(mocked_manager, mocked_listener, mocked_logger)
