import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

def visualizeCorrelation(data, username1, username2):
    plt.style.use('ggplot')

    user_ratings1 = data[username1]
    user_ratings2 = data[username2]

    user_keys1 = set(user_ratings1)
    user_keys2 = set(user_ratings2)
    matching_keys = user_keys1.intersection(user_keys2)

    x = np.array([user_ratings1[k] for k in matching_keys])
    y = np.array([user_ratings2[k] for k in matching_keys])

    slope, intercept, r, p, stderr = scipy.stats.linregress(x, y)
    line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.3f}'

    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=0, marker='s', label='Data points')
    ax.plot(x, intercept + slope * x, label=line)
    ax.set_xlabel(username1)
    ax.set_ylabel(username2)
    ax.legend(facecolor='white')
    plt.show()