ScreenPy Adapter: Allure
========================

[![Build Status](../../actions/workflows/tests.yml/badge.svg)](../../actions/workflows/tests.yml)
[![Build Status](../../actions/workflows/lint.yml/badge.svg)](../../actions/workflows/lint.yml)

[![Supported Versions](https://img.shields.io/pypi/pyversions/screenpy_adapter_allure.svg)](https://pypi.org/project/screenpy_adapter_allure)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

```
TITLE CARD:
                         "ScreenPy Adapter: Allure"
TITLE DISAPPEARS.
                                                                      FADE IN:
INT. DOCUMENTATION - UNKNOWN TIME

A recording room door opens and AUDIENCE peeks inside. AUDIENCE quietly steps
over cords and around chairs, approaching the switchboard. NARRATOR quietly
resumes their guidance.

                              NARRATOR (V.O.)
            Ah, this is one of the Adapters for my microphone. This
            one sends them to an Allure report.

                              AUDIENCE
                              (hushed)
            You mean you have a literal microphone, and that's how
            you're talking to me? I thought I had been stingy to
            some tester and you were the first of three spirits.

                              NARRATOR (V.O.)
            Not a literal microphone, but it's a helpful metaphor.

                              AUDIENCE
                              (hushed)
            That's not as helpful as you think it is, when your
            voice is in my head.

A beat, as AUDIENCE looks appraisingly at the equipment.

                              AUDIENCE (CONT'D)
                              (hushed)
            This looks complicated. I'm leaving now.

                              NARRATOR (V.O.)
            Let's turn left outside the door...

                                                                      FADE OUT
```


Installation
------------
    pip install screenpy_adapter_allure

or

    pip install screenpy[allure]


Documentation
-------------
Please check out the [Read The Docs documentation](https://screenpy-adapter-allure-docs.readthedocs.io/en/latest/) for the latest information about this module!

You can also read the [ScreenPy Docs](https://screenpy-docs.readthedocs.io/en/latest/) for more information about ScreenPy in general.


Contributing
------------
You want to contribute? Great! Here are the things you should do before submitting your PR:

1. Fork the repo and git clone your fork.
1. `dev` install the project package:
    1. `pip install -e .[dev]`
    1. Optional (poetry users):
        1. `poetry install --extras dev`
1. Run `pre-commit install` once.
1. Run `tox` to perform tests frequently.
1. Create pull-request from your branch.

That's it! :)
