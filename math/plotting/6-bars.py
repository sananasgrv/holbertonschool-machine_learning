#!/usr/bin/env python3
"""
Complete the following
    source code to plot a stacked bar graph:
"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
    fruit
    """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    people = np.array(["Farrah", "Fred", "Felicia"])

    fruit_names = {
        "apples": fruit[0],
        "bananas": fruit[1],
        "oranges": fruit[2],
        "peaches": fruit[3],
    }

    colors = {
        "apples": "red",
        "bananas": "yellow",
        "oranges": "#ff8000",
        "peaches": "#ffe5b4",
    }

    plt.figure(figsize=(6.4, 4.8))
    width = 0.5
    bottom = np.zeros(3)

    for name, value in fruit_names.items():
        plt.bar(
            people,
            value,
            width,
            label=name,
            bottom=bottom,
            color=colors[name]
        )
        bottom += value

    plt.ylim(0, 80)
    plt.title("Number of Fruit per Person")
    plt.ylabel("Quantity of Fruit")
    plt.legend(loc="upper right")
    plt.show()
