import sys

from cmd.commands import SetupCommand, StartCommand, Command
from cmd.strategies import OneConnectionPerSimulationStrategy, NewConnectionPerQueryStrategy, ConnectionPoolStrategy


class CommandLineParser:
    commands: dict

    def __init__(self, credentials: dict):
        strategies = [
            NewConnectionPerQueryStrategy(credentials, int(sys.argv[3])),
            OneConnectionPerSimulationStrategy(credentials, int(sys.argv[3])),
            ConnectionPoolStrategy(credentials, int(sys.argv[3]))
        ]
        self.commands = {
            "setup": SetupCommand(credentials),
            "start": StartCommand(strategies, credentials)
        }

    def get_command(self, cmd: str) -> Command:
        return self.commands[cmd]
