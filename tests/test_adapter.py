from unittest import mock

import pytest
from screenpy.exceptions import UnableToNarrate

from screenpy_adapter_allure import AllureAdapter


def prop():
    """The revolver in the foyer!"""
    pass


@mock.patch("screenpy_adapter_allure.adapters.allure")
class TestAllureAdapter:
    @pytest.mark.parametrize(
        "narrator_level,allure_level", AllureAdapter.GRAVITAS.items()
    )
    def test_act(self, mocked_allure, narrator_level, allure_level):
        adapter = AllureAdapter()
        act_name = "test act"
        test_func = adapter.act(prop, act_name, narrator_level)

        next(test_func)()

        mocked_allure.epic.assert_called_once_with(act_name)
        mocked_allure.severity.assert_called_once_with(allure_level)

    @pytest.mark.parametrize(
        "narrator_level,allure_level", AllureAdapter.GRAVITAS.items()
    )
    def test_scene(self, mocked_allure, narrator_level, allure_level):
        adapter = AllureAdapter()
        scene_name = "test scene"
        test_func = adapter.scene(prop, scene_name, narrator_level)

        next(test_func)()

        mocked_allure.feature.assert_called_once_with(scene_name)
        mocked_allure.severity.assert_called_once_with(allure_level)

    @pytest.mark.parametrize(
        "narrator_level,allure_level", AllureAdapter.GRAVITAS.items()
    )
    def test_beat(self, mocked_allure, narrator_level, allure_level):
        adapter = AllureAdapter()
        beat_message = "test beat"
        test_func = adapter.beat(prop, beat_message, narrator_level)

        next(test_func)()

        mocked_allure.step.assert_called_once_with(beat_message)
        mocked_allure.severity.assert_called_once_with(allure_level)

    def test_embedded_beat_allure_message(self, mocked_allure):
        """Context deepens with the embedded beats."""
        adapter = AllureAdapter()

        # yeah, this is weird. The beat method returns a generator, and we
        # need to keep it open. This is the most straightforward way!
        for func1 in adapter.beat(prop, "1"):
            for func2 in adapter.beat(func1, "2"):
                for func3 in adapter.beat(func2, "3"):
                    func3()

        calls = mocked_allure.step.mock_calls
        assert len(calls) == 9
        assert calls[0][1][0] == "1"
        assert calls[1][0] == "().__enter__"
        assert calls[2][1][0] == "2"
        assert calls[3][0] == "().__enter__"
        assert calls[4][1][0] == "3"
        assert calls[5][0] == "().__enter__"
        assert calls[6][0] == "().__exit__"
        assert calls[7][0] == "().__exit__"
        assert calls[8][0] == "().__exit__"

    @pytest.mark.parametrize(
        "narrator_level,allure_level", AllureAdapter.GRAVITAS.items()
    )
    def test_aside(self, mocked_allure, narrator_level, allure_level):
        adapter = AllureAdapter()
        aside_message = "test aside"
        test_func = adapter.aside(prop, aside_message, narrator_level)

        next(test_func)()

        mocked_allure.step.assert_called_once_with(aside_message)
        mocked_allure.severity.assert_called_once_with(allure_level)

    def test_error(self, mocked_manager, mock_allure_trappings):
        adapter = AllureAdapter()
        mocked_logger = mock_allure_trappings.logger

        for _ in adapter.beat(prop, "We named the dog Indiana."):
            adapter.error(ValueError("It belongs in a museum!"))

        mocked_logger.stop_step.assert_called_once()

    def test_attach(self, mocked_allure):
        adapter = AllureAdapter()
        test_path = "ddouglas/documents/freak_out.png"
        test_name = "Dexter Douglas"
        test_attachment_type = ("nerd", "computer ace")
        test_extension = "cyberspace"

        adapter.attach(
            test_path,
            name=test_name,
            attachment_type=test_attachment_type,
            extension=test_extension,
        )

        mocked_allure.attach.file.assert_called_once_with(
            test_path, test_name, test_attachment_type, test_extension
        )

    def test_attach_raises_if_no_attachment_type(self, mocked_allure):
        adapter = AllureAdapter()

        with pytest.raises(UnableToNarrate):
            adapter.attach("foo")
