import screenpy_adapter_allure


def test_screenpy_adapter_allure() -> None:
    expected = [
        "AllureAdapter",
    ]
    assert sorted(screenpy_adapter_allure.__all__) == sorted(expected)
