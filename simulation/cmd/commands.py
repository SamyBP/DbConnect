from typing import List

import psycopg2

from cmd import strategies
from db import setup


class Command:
    credentials: dict

    def __init__(self, credentials: dict):
        self.credentials = credentials

    def execute(self):
        pass


class SetupCommand(Command):

    def __init__(self, credentials: dict):
        super().__init__(credentials)

    def execute(self):
        print("Setup: trying to establish connection")
        connection = psycopg2.connect(
            database=self.credentials.get("database"),
            user=self.credentials.get("user"),
            password=self.credentials.get("password")
        )
        print("Setup: connection established, creating test table")
        setup.create_test_table(connection)
        print("Setup: table created, closing connection")
        connection.close()
        print("Setup: connection closed")


class StartCommand(Command):
    strategies: List[strategies.Strategy]

    def __init__(self, credentials: dict):
        super().__init__(credentials)
        self.strategies = [
            strategies.NewConnectionPerQueryStrategy(),
            strategies.OneConnectionPerSimulationStrategy(),
            strategies.ConnectionPoolStrategy()
        ]

    def execute(self):
        for strategy in self.strategies:
            strategy.apply()
