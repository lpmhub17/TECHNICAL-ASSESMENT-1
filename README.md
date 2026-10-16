Random Walk Simulation
This Python program simulates multiple agents moving randomly on a square grid. Each agent moves one space at a time in a random direction: up, down, left, or right.
The agents are prevented from moving outside the grid. Their movement is displayed using a live Matplotlib animation.
Requirements
- Python 3.x
- Matplotlib
Install Matplotlib with:
py -m pip install matplotlib
If the py command does not work, try:
python -m pip install matplotlib
How to Run
1. Open the project folder in VS Code.
2. Open the terminal in VS Code.
3. Run the program:
py random_walk.py
You can also run it with:
python random_walk.py
User Inputs
The program asks for three values:
1. Number of agents – the number of moving points on the grid.
2. Grid size – the size of the square grid. For example, entering 10 creates a 10x10 grid.
3. Number of steps – how many movements the animation will display.
Example:
Enter the number of agents: 5
Enter the grid size (e.g., 10 for a 10x10 grid): 10
Enter number of steps: 50
How It Works
- Each agent receives a random starting position.
- During every step, each agent randomly chooses one of four directions.
- Boundary checks keep the agents inside the grid.
- The graph updates after every step to show the agents' new positions.
Important Note
This version does not require the agentpy package. It uses standard Python, random, and matplotlib, making it easier to run in VS Code.
Possible Applications
This simulation can represent simplified versions of:
- Particle diffusion
- Crowd movement
- Animal movement
- Pollution spreading
- Random movement of cells or microorganis
