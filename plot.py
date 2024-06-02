import matplotlib.pyplot as plt

def plot_objects(obj1, obj2, title="Objects"):
    plt.figure(figsize=(8, 8))
    plt.plot(obj1[:, 0], obj1[:, 1], label='Object 1')
    plt.plot(obj2[:, 0], obj2[:, 1], label='Object 2')
    plt.scatter(obj1[:, 0], obj1[:, 1])
    plt.scatter(obj2[:, 0], obj2[:, 1])
    plt.axhline(0, color='grey', linewidth=0.5)
    plt.axvline(0, color='grey', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()