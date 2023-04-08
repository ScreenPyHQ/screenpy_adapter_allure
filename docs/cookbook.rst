=======
Recipes
=======

This plugin is an adapter for the microphone of ScreenPy's Narrator which sends logs to Allure.

This `example <https://github.com/ScreenPyHQ/screenpy_examples/tree/trunk/screenpy_selenium/github>`__ makes use of this plugin.

Rationale
=========

Without this plugin when you generate a test report using allure it will display as follow

.. image:: ./allure_without_plugin.png
  :width: 768
  :alt: Screenshot without plugin has not the steps

Plugging In the Adapter
=======================

Plugging the ``AllureAdapter``
into the :external+screenpy:ref:`Narrator <narration>`'s microphone
must be done during test setup.
This will be in your ``conftest.py`` file for `pytest <https://docs.pytest.org/>`__,
or during suite configuration for `unittest <https://docs.python.org/3/library/unittest.html>`__.

Either way,
the steps are the same,
wherever you need to do them::

    from screenpy.pacing import the_narrator
    from screenpy_adapter_allure import AllureAdapter

    the_narrator.attach_adapter(AllureAdapter())

After that the steps are attached to the allure report

.. image:: ./allure_with_plugin.png
  :width: 768
  :alt: Screenshot without plugin has not the steps

Attach Screenshot from selenium
===============================

If you are using allure in a selenium project using `ScreenpPy Selenium <https://screenpy-selenium-docs.readthedocs.io/en/latest/>`__

You can attach a new screenshot to the report using the action `SaveScreenshot <https://screenpy-selenium-docs.readthedocs.io/en/latest/extended_api/actions.html#screenpy_selenium.actions.SaveScreenshot>`__

For example you can attach an screenshot as PNG::

    from screenpy import Actor
    from allure_commons.types import AttachmentType

    filepath = 'screenshot.png'

    the_actor = Actor.named("Perry").who_can(BrowseTheWeb.using_firefox())

    the_actor.attempts_to(
        SaveScreenshot.as_(filepath).and_attach_it_with(
            attachment_type=AttachmentTypes.PNG,
        ),
    )

In the github example we go to the github page and find the `screenpy_examples` repository

.. image:: ./allure_screenshot.png
  :width: 768
  :alt: Allure report showing the screenshot from the Github example
