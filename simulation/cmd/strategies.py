import threading
import time

from cmd import constants
from db import db


class Strategy:
    duration_ns: int
    credentials: dict

    def __init__(self, credentials: dict, duration_min: int):
        self.credentials = credentials
        self.duration_ns = duration_min * constants.MIN_TO_NANO

    def apply(self):
        pass


class NewConnectionPerQueryStrategy(Strategy):

    def __init__(self, credentials: dict, duration_min: int):
        super().__init__(credentials, duration_min)

    def apply(self):
        end_time = time.time_ns() + self.duration_ns
        while time.time_ns() < end_time:
            connection = db.get_connection(self.credentials)
            db.add_entry(connection)
            connection.close()


class OneConnectionPerSimulationStrategy(Strategy):

    def __init__(self, credentials: dict, duration_min: int):
        super().__init__(credentials, duration_min)
        self.connection = db.get_connection(credentials)

    def apply(self):
        end_time = time.time_ns() + self.duration_ns
        while time.time_ns() < end_time:
            db.add_entry(self.connection)
        self.connection.close()


class ConnectionPoolStrategy(Strategy):

    def __init__(self, credentials: dict, duration_min: int, thread_count: int = 2):
        super().__init__(credentials, duration_min)
        self.connection_pool = db.get_connection_pool(credentials)
        self.thread_count = thread_count
        self.stop_threads = threading.Event()

    def apply(self):
        threads = self.__create_threads()
        simulation_time = self.duration_ns / constants.NANO_TO_SEC
        time.sleep(simulation_time)
        self.stop_threads.set()
        self.__join_threads(threads)

    def __create_threads(self):
        threads = list()
        for _ in range(self.thread_count):
            th = threading.Thread(target=self.__run_query)
            threads.append(th)
            th.start()
        return threads

    def __run_query(self):
        while not self.stop_threads.is_set():
            connection = self.connection_pool.getconn()
            db.add_entry(connection)
            self.connection_pool.putconn(connection)

    def __join_threads(self, threads):
        for th in threads:
            th.join()
