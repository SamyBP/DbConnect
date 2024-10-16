import numpy as np
import matplotlib.pyplot as plt


def figure(data: dict):
    strategies = list(data.keys())
    values = list(data.values())
    fig = plt.figure(figsize=(10, 5))
    plt.bar(strategies, values, color='blue', width=0.4)
    plt.xlabel("Connection strategy")
    plt.ylabel("Insert count")
    plt.title("Connection strategy performance analysis")
    plt.show()
