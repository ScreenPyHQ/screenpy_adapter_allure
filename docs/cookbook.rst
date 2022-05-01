=======
Recipes
=======

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
