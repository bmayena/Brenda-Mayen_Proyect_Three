# 🎯 Galton Board Simulation
📌 Description
This project simulates the behavior of a Galton board using Python functions and generates a graphical representation with .

# ⚙️ Program Features
• 	Simulates a Galton machine with 3000 beads.
• 	The board has 12 levels of obstacles, where each bead makes a decision (left or right) at each level.
• 	The final result is displayed as a histogram showing the number of beads in each bin.
• 	The program uses two main functions:
  	One to calculate the final position of the beads.
  	One to plot the histogram.

# 🧠Simulation Logic
To understand the simulation, it's important to grasp how a bead behaves as it falls:
1. 	The number of bins equals the number of rows + 1.
2. 	At each row, the bead can go left or right.
3. 	Each bead makes N decisions, where N is the number of rows.
👉 The final position of a bead depends solely on how many times it went to the right. This graphic representation let this clear:

![Galton board for one bead](https://github.com/bmayena/Brenda-Mayen_Proyect_Three/blob/main/galton%20board.jpg)

# 🧪 Program Functions
🔹 Simulating a single bead
def simulate_ball(levels):
    right = 0
    for _ in range(levels):
        step = random.choice([0, 1])  # 0 = left, 1 = right 
        right += step
    return right

This function simulates the path of a bead through the board. Only right steps are counted to determine the final bin.

🔹 Simulating the entire board
def simulate_board(ball_count, levels):
    results = [0] * (levels + 1)  
    for _ in range(ball_count):
        position = simulate_ball(levels)
        results[position] += 1
    return results

Applies the single bead simulation to all beads. Returns a list with the count of beads in each bin.


🔹 Plotting the histogram
def plot_results(results):
    positions = list(range(len(results)))
    plt.bar(positions, results, color='skyblue', edgecolor='black') #set graphics
    plt.title('Distribution in the Galton Board') #title
    plt.xlabel('Bin') #label x
    plt.ylabel('Number of beads') #label y
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

Generates a histogram using the "results" list, showing the final distribution of the 3000 simulated beads.

# 📝 Conclusions
This exercise is especially useful to highlight the importance of understanding the logic behind what we want to code before jumping into implementation.
While developing this program, I had doubts about the best way to determine each bead’s final position. The process became clearer when I sketched a simulation on paper. I also used AI tools to realize that simply counting the number of times a bead goes to the right is enough to determine its final bin.
