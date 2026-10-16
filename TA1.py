import random 
import matplotlib.pyplot as plt 
import matplotlib.animation as animation 
 
# Get user input 
num_agents = int(input("Enter the number of agents: ")) 
grid_size = int(input("Enter the grid size (e.g., 10 for a 10x10 grid): ")) 
num_steps = int(input("Enter number of steps: ")) 
 
# Store each agent's position 
agents = [ 
    [ 
        random.randint(0, grid_size - 1), 
        random.randint(0, grid_size - 1) 
    ] 
    for _ in range(num_agents) 
] 
 
# Set up the graph 
fig, ax = plt.subplots() 
 
ax.set_xlim(-0.5, grid_size - 0.5) 
ax.set_ylim(-0.5, grid_size - 0.5) 
ax.set_xticks(range(grid_size)) 
ax.set_yticks(range(grid_size)) 
ax.grid(True) 
 
scatter = ax.scatter([], [], s=200, color="blue") 
 
 
def update(frame): 
    directions = [ 
        (1, 0), 
        (-1, 0), 
        (0, 1), 
        (0, -1) 
    ] 
 
    # Move every agent 
    for agent in agents: 
        dx, dy = random.choice(directions) 
 
        agent[0] += dx 
        agent[1] += dy 
 
        # Keep agents inside the grid 
        agent[0] = max(0, min(grid_size - 1, agent[0])) 
        agent[1] = max(0, min(grid_size - 1, agent[1])) 
 
    # Update displayed positions 
    positions = [(agent[0], agent[1]) for agent in agents] 
    scatter.set_offsets(positions) 
 
    ax.set_title(f"Step {frame + 1}/{num_steps}") 
 
    return scatter, 
 
 
# Create animation 
  
ani = animation.FuncAnimation( 
fig, 
update, 
frames=num_steps, 
interval=300, 
blit=True, 
repeat=False 
) 
plt.show() 