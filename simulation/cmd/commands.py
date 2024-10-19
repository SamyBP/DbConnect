import datetime

from datetime import datetime
from typing import List

from cmd import plot
from cmd.strategies import Strategy
from db import db


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
        connection = db.get_connection(self.credentials)
        print("Setup: connection established, creating test table")
        db.create_test_table(connection)
        print("Setup: table created, closing connection")
        connection.close()
        print("Setup: connection closed")


class StartCommand(Command):
    strategies: List[Strategy]

    def __init__(self, strategies: List[Strategy], credentials: dict):
        super().__init__(credentials)
        self.strategies = strategies

    def execute(self):
        results = {}
        for strategy in self.strategies:
            strategy_name = strategy.__class__.__name__
            print(f"[{datetime.now()}] Applying strategy: {strategy_name}:")
            strategy.apply()
            connection = db.get_connection(self.credentials)
            insert_count = db.get_number_of_inserts(connection)
            results[strategy_name] = insert_count
            print(f"[{datetime.now()}] Strategy: {strategy_name} applied. Total insert count is:{insert_count}")
            print(f"[{datetime.now()}] Running cleanup between tests:")
            db.cleanup_between_tests(connection)
            connection.close()
        plot.figure(results)
