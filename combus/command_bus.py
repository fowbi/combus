from combus.command import Command
from combus.command_handler import CommandHandler


class CommandBus:
    """Accepts and distributes commands to available handler.

    Example:
        commandbus = CommandBus()
        commandbus.link_with_handler(FooCommand.__class__, FooHandler())
        commandbus.handle(FooCommand(bar='bar'))
    """
    def __init__(self):
        self.handlers = {}

    def handle(self, command: Command):
        """Distribute given command to one of the defined handlers.
        The command is discarded if no handler was defined for the given command.

        Args:
            command (Command): Command that we would like to handle.

        Returns:
            void
        """
        handler_name = type(command).__name__
        if handler_name in self.handlers:
            self.handlers[handler_name](command)

    def link_command_with_handler(self, command: str, handler: CommandHandler):
        """Add a link between a command an a handler.
        Adding a new handler with an already defined command name, will overwrite the first one.

        Args:
            command (str): Command name, use the __name__ of the command.
            handler (CommandHandler): The handler to execute when we put the a command on the bus.

        Returns:
            void
        """
        self.handlers[command] = handler
