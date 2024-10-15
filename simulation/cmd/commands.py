from typing import List

import psycopg2

from cmd.strategies import Strategy
from db import queries, util


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
        connection = util.get_connection(self.credentials)
        print("Setup: connection established, creating test table")
        queries.create_test_table(connection)
        print("Setup: table created, closing connection")
        connection.close()
        print("Setup: connection closed")


class StartCommand(Command):
    strategies: List[Strategy]

    def __init__(self, strategies: List[Strategy], credentials: dict):
        super().__init__(credentials)
        self.strategies = strategies

    def execute(self):
        for strategy in self.strategies:
            print(f"Applying strategy: {strategy.__class__.__name__}:")
            strategy.apply()
            connection = util.get_connection(self.credentials)
            insert_count = queries.get_number_of_inserts(connection)
            print(f"Strategy: {strategy.__class__.__name__} applied. Total insert count is:{insert_count}")
            print(f"Running cleanup between tests:")
            queries.cleanup_between_tests(connection)
            connection.close()

