#!/usr/bin/env python3
"""
Complete the following source code
    to plot all 5 previous graphs in one figure:
"""
import numpy as np
import matplotlib.pyplot as plt


def all_in_one():
    """
    All axis labels and plot titles should have
        a font size of x-small (to fit nicely in one figure)
    The plots should make a 3 x 2 grid
    The last plot should take up two column widths (see below)
    The title of the figure should be All in One
    """
    fig = plt.figure(figsize=(6.4, 4.8))
    fig.suptitle("All in One")
    gr= fig.add_gridspec(3, 2)
    f1 = fig.add_subplot(gr[0, 0])
    f2 = fig.add_subplot(gr[0, 1])
    f3 = fig.add_subplot(gr[1, 0])
    f4 = fig.add_subplot(gr[1, 1])
    f5 = fig.add_subplot(gr[2, :])


    y0 = np.arange(0, 11) ** 3
    f1.plot(y0, color="red")
    f1.set_xlim([0, 10])


    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
    y1 += 180
    f2.scatter(x1, y1, color="magenta")
    f2.set_title("Men's Height vs Weight", fontsize="x-small")
    f2.set_xlabel("Height (in)", fontsize="x-small")
    f2.set_ylabel("Weight (lbs)", fontsize="x-small")


    x2 = np.arange(0, 28651, 5730)
    r2 = np.log(0.5)
    t2 = 5730
    y2 = np.exp((r2 / t2) * x2)
    f3.set_xlabel("Time (years)", fontsize="x-small")
    f3.set_ylabel("Fraction Remaining", fontsize="x-small")
    f3.set_title("Exponential Decay of C-14", fontsize="x-small")
    f3.set_xlim(0, 28650)
    f3.set_yscale("log")
    f3.plot(x2, y2)


    x3 = np.arange(0, 21000, 1000)
    r3 = np.log(0.5)
    t31 = 5730
    t32 = 1600
    y31 = np.exp((r3 / t31) * x3)
    y32 = np.exp((r3 / t32) * x3)
    f4.set_title("Exponential Decay of Radioactive Elements", fontsize="x-small")
    f4.set_xlabel("Time (years)", fontsize="x-small")
    f4.set_ylabel("Fraction Remaining", fontsize="x-small")
    f4.set_xlim(0, 20000)
    f4.set_ylim(0, 1)
    f4.plot(x3, y31, color="red", ls="--", label="C-14")
    f4.plot(x3, y32, color="green", label="Ra-226")
    f4.legend(loc="upper right")


    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    bins1 = np.arange(0, 101, 10)
    f5.set_title("Project A", fontsize="x-small")
    f5.set_xlabel("Grades", fontsize="x-small")
    f5.set_ylabel("Number of Students", fontsize="x-small")
    f5.hist(student_grades, bins=bins1, edgecolor="black")
    f5.set_xlim(0, 100)
    f5.set_ylim(0, 30)
    f5.set_xticks(bins1)

    plt.tight_layout()
    plt.show()
