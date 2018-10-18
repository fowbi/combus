Combus
=======

.. image:: https://travis-ci.com/fowbi/combus.svg?branch=master
    :target: https://travis-ci.com/fowbi/combus

combus is a simple commandbus for Python 3.7+

Installation
=============

pipenv:

.. code:: bash

    pipenv install combus

pip:

.. code:: bash

    pip install combus

From source:

.. code:: bash

    python setup.py install

Usage
======

.. code:: python

    class FooHandler(CommandHandler):
        def _handle(self, command: Command):
            # do something with the command

    class FooCommand(Command):
        def __init__(self, foo):
            self._foo = foo

        @property
        def foo(self):
            return self._foo

    bus = CommandBus()
    bus.link_command_with_handler(FooCommand.__name__, FooHandler())
    bus.handle(FooCommand(foo="bar"))
