from combus.command import Command


class CommandHandler:
    """Handler for any given command.

    Example:
        class FooHandler(CommandHandler):
            def _handle(self, command: Command):
                print('Do something with the command')

        handler = FooHandler()
        handler(FooCommand(bar='bar'))
    """
    def __call__(self, command: Command):
        """Handle single command.

        Args:
            command (Command): Command to handle.

        Returns:
            void
        """
        self._handle(command)

    def _handle(self, command: Command):
        """Implementation of the handling. Defined in the extended method.

        Args:
            command (Command): Command to handle.

        Returns:
            void
        """
        raise NotImplementedError()
