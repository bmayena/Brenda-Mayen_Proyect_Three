#Galton board simulation
#For 3000 beads and 12 pegs (or rows)

import random
import matplotlib.pyplot as plt

# Function to simulate the path of a ball
def simulate_ball(levels):
    right = 0
    for _ in range(levels):
        step = random.choice([0, 1])  # 0 = left, 1 = right This simulates each of the movement possibilities that the bead has.
        right += step
    return right

# Function to simulate many balls or beads 
def simulate_board(ball_count, levels):
    results = [0] * (levels + 1)  # Results or bins/ List to count beads in each container
    for _ in range(ball_count):
        position = simulate_ball(levels)
        results[position] += 1
    return results

# Function to plot the results
def plot_results(results):
    positions = list(range(len(results)))
    plt.bar(positions, results, color='purple', edgecolor='black') #set graphics
    plt.title('Distribution in the Galton Board') #title
    plt.xlabel('Bin') #label x
    plt.ylabel('Number of beads') #label y
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

# Simulation parameters
levels = 12 #rows or pegs
ball_count = 3000 #balls or beads 

# Run simulation
results = simulate_board(ball_count, levels) 
#print(results) just for check
# Plot
plot_results(results)