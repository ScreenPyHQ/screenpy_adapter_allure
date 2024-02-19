import logging
from itertools import permutations
from typing import Generator, Any
from unittest import mock

from _pytest.fixtures import SubRequest
import pytest
from screenpy import Narrator
from screenpy.narration.gravitas import NORMAL
from screenpy.narration.stdout_adapter import StdOutAdapter, settings
from screenpy.pacing import act, aside, beat, scene, the_narrator

from screenpy_adapter_allure import AllureAdapter

TEST_ACT = "Three"
TEST_SCENE = "The Scene Where He Uses It"
TEST_BEAT = "Don't make me use this!"
TEST_ASIDE = "You made me use it!!"
TEST_RETVAL = ">:("
INDENT = settings.INDENT_CHAR * settings.INDENT_SIZE


@act(TEST_ACT, gravitas=NORMAL)
@scene(TEST_SCENE)
def prop() -> None:
    pass


class Prop:
    @beat(TEST_BEAT)
    def use(self) -> str:
        aside(TEST_ASIDE)
        return TEST_RETVAL


def _assert_allure_correct(mocked_allure: mock.Mock) -> None:
    """Assert the correctness of the calls to allure."""
    mocked_allure.epic.assert_called_once_with(TEST_ACT)
    mocked_allure.feature.assert_called_once_with(TEST_SCENE)
    mocked_allure.severity.assert_called_once_with(AllureAdapter.GRAVITAS[NORMAL])
    step_calls = mocked_allure.step.mock_calls
    assert len(step_calls) == 9
    assert step_calls[0][1][0] == TEST_BEAT
    assert step_calls[1][0] == "().__enter__"
    assert step_calls[2][1][0] == TEST_ASIDE
    assert step_calls[3][0] == "().__enter__"
    assert step_calls[4][0] == "().__exit__"
    assert step_calls[5][1][0] == f"=> {TEST_RETVAL}"
    assert step_calls[6][0] == "().__enter__"
    assert step_calls[7][0] == "().__exit__"
    assert step_calls[8][0] == "().__exit__"


def _assert_stdout_correct(caplog: pytest.LogCaptureFixture) -> None:
    """Assert the correctness of logged messages to stdout.

    Copied from screenpy/tests/test_narration_integration.
    """
    assert len(caplog.messages) == 5
    assert caplog.messages[0] == f"ACT {TEST_ACT.upper()}"
    assert caplog.messages[1] == f"Scene: {TEST_SCENE.title()}"
    assert caplog.messages[2] == TEST_BEAT
    assert caplog.messages[3] == f"{INDENT}{TEST_ASIDE}"
    assert caplog.messages[4] == f"{INDENT}=> {TEST_RETVAL}"


@mock.patch("screenpy_adapter_allure.adapters.allure")
class TestNarrateToAllure:
    @pytest.fixture(autouse=True)
    def narrator_has_allure(self) -> Generator[Narrator, Any, None]:
        old_adapters = the_narrator.adapters
        the_narrator.adapters = [AllureAdapter()]
        yield the_narrator
        the_narrator.adapters = old_adapters

    def test_narrations(self, mocked_allure: mock.Mock) -> None:
        # We need to create this in here, so it uses the mocked allure
        @act(TEST_ACT, gravitas=NORMAL)
        @scene(TEST_SCENE)
        def allure_prop() -> None:
            pass

        allure_prop()
        Prop().use()

        _assert_allure_correct(mocked_allure)

    def test_flushed_narrations(self, mocked_allure: mock.Mock) -> None:
        # We need to create this in here, so it uses the mocked allure
        @act(TEST_ACT, gravitas=NORMAL)
        @scene(TEST_SCENE)
        def allure_prop() -> None:
            pass

        with the_narrator.mic_cable_kinked():
            allure_prop()
            Prop().use()

        _assert_allure_correct(mocked_allure)


@mock.patch("screenpy_adapter_allure.adapters.allure")
class TestNarrateToAll:
    @pytest.fixture(
        autouse=True, params=permutations([AllureAdapter(), StdOutAdapter()])
    )
    def narrator_has_all(self, request: SubRequest) -> Generator[Narrator, Any, None]:
        """Give Narrator all adapters in all orders."""
        old_adapters = the_narrator.adapters
        the_narrator.adapters = request.param
        yield the_narrator
        the_narrator.adapters = old_adapters

    def test_narration(
        self, mocked_allure: mock.Mock, caplog: pytest.LogCaptureFixture
    ) -> None:
        mocked_allure.epic.return_value = lambda f: f
        mocked_allure.feature.return_value = lambda f: f
        mocked_allure.severity.return_value = lambda f: f

        # We need to create this in here, so it uses the mocked allure
        @act(TEST_ACT, gravitas=NORMAL)
        @scene(TEST_SCENE)
        def allure_prop() -> None:
            pass

        with caplog.at_level(logging.INFO):
            allure_prop()
            Prop().use()

        _assert_allure_correct(mocked_allure)
        _assert_stdout_correct(caplog)

    def test_flushed_narration(
        self, mocked_allure: mock.Mock, caplog: pytest.LogCaptureFixture
    ) -> None:
        mocked_allure.epic.return_value = lambda f: f
        mocked_allure.feature.return_value = lambda f: f
        mocked_allure.severity.return_value = lambda f: f

        # We need to create this in here, so it uses the mocked allure
        @act(TEST_ACT, gravitas=NORMAL)
        @scene(TEST_SCENE)
        def allure_prop() -> None:
            pass

        with caplog.at_level(logging.INFO):
            with the_narrator.mic_cable_kinked():
                allure_prop()
                Prop().use()

        _assert_allure_correct(mocked_allure)
        _assert_stdout_correct(caplog)
