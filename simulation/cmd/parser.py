from cmd.commands import SetupCommand, StartCommand, Command


class CommandLineParser:
    commands: dict

    def __init__(self, credentials: dict):
        self.commands = {
            "setup": SetupCommand(credentials),
            "start": StartCommand(credentials)
        }

    def get_command(self, cmd: str) -> Command:
        return self.commands[cmd]
