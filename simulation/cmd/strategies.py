class Strategy:

    def apply(self):
        pass


class NewConnectionPerQueryStrategy(Strategy):

    def apply(self):
        print("NewConnectionPerQuery")


class OneConnectionPerSimulationStrategy(Strategy):

    def apply(self):
        print("OneConnectionPerSimulation")


class ConnectionPoolStrategy(Strategy):

    def apply(self):
        print("ConnectionPool")
