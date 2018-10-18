from combus.command import Command
from combus.command_bus import CommandBus
from combus.command_handler import CommandHandler


def test_it_will_handle_a_command():
    class Bar(object):
        def __init__(self):
            self._foo = None

        @property
        def foo(self):
            return self._foo

        @foo.setter
        def foo(self, foo):
            self._foo = foo

    class FooHandler(CommandHandler):
        def __init__(self, helper: Bar):
            self.helper = helper

        def _handle(self, command: Command):
            self.helper.foo = command.foo

    class FooCommand(Command):
        def __init__(self, foo):
            self._foo = foo

        @property
        def foo(self):
            return self._foo

    helper = Bar()
    bus = CommandBus()
    bus.link_command_with_handler(FooCommand.__name__, FooHandler(helper=helper))

    bus.handle(FooCommand(foo="bar"))

    assert 'bar' == helper.foo
