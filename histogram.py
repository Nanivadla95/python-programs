import random
import matplotlib.pyplot as plt

def simulate_throws(num_dice, num_sides, num_throws):
    sums = []
    for _ in range(num_throws):
        throw_sum = sum(random.randint(1, num_sides) for _ in range(num_dice))
        sums.append(throw_sum)
    return sums

def plot_normalized_histogram(sums, num_dice, num_sides):
    # Calculate the histogram
    min_sum = num_dice
    max_sum = num_dice * num_sides
    bins = range(min_sum, max_sum + 2)  # +2 to include the last edge

    # Normalize the histogram
    counts, edges = plt.histogram(sums, bins=bins, density=True)
    
    # Plot the normalized histogram
    plt.bar(edges[:-1], counts, width=1, edgecolor='black', align='center')
    plt.xticks(range(min_sum, max_sum + 1))
    plt.xlabel('Sum of Dice')
    plt.ylabel('Normalized Frequency')
    plt.title(f'Normalized Histogram of Sums for {num_dice} {num_sides}-sided Dice')
    plt.show()

# Parameters
num_dice = 3  # Number of dice
num_sides = 6  # Number of sides on each die
num_throws = 10000  # Number of throws to simulate

# Simulate throws
sums = simulate_throws(num_dice, num_sides, num_throws)

# Plot normalized histogram
plot_normalized_histogram(sums, num_dice, num_sides)
