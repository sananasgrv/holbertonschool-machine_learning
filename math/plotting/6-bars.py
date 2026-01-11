#!/usr/bin/env python3
"""
Complete the following
    source code to plot a stacked bar graph:
"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
    fruit is a matrix representing the number of fruit various people possess
    The columns of fruit represent the number of fruit Farrah, Fred, and Felicia have, respectively
    The rows of fruit represent the number of apples, bananas, oranges, and peaches, respectively
    The bars should represent the number of fruit each person possesses:
    The bars should be grouped by person, i.e, the horizontal axis should have one labeled tick per person
    Each fruit should be represented by a specific color:
    apples = red
    bananas = yellow
    oranges = orange (#ff8000)
    peaches = peach (#ffe5b4)
    A legend should be used to indicate which fruit is represented by each color
    The bars should be stacked in the same order as the rows of fruit, from bottom to top
    The bars should have a width of 0.5
    The y-axis should be labeled Quantity of Fruit
    The y-axis should range from 0 to 80 with ticks every 10 units
    """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4,3))
    people = np.array(["Farrah", "Fred", "Felicia"])
    fruit_names = {
        "apples":fruit[0] ,
        "bananas":fruit[1] ,
        "oranges":fruit[2] ,
        "peaches":fruit[3] ,
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
        plt.bar(people, value, width, label=name, bottom=bottom, color=colors[name])
        bottom += value
    plt.ylim(0, 80)

    plt.title("Number of Fruit per Person")
    plt.ylabel("Quantity of Fruit")
    plt.legend(loc="upper right")
    plt.show()
