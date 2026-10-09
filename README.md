# Warehouse Robot Management System

**Live simulator:** [robotwarehouse.dhruvpathak.com](https://robotwarehouse.dhruvpathak.com)

## Project Overview
This project simulates a central planner that moves a mixed fleet of robots across an $N \times N$ warehouse grid. Each robot has a start cell and a goal cell. Every step, the planner proposes one move per robot, detects conflicts between robots that want the same cell, and decides who goes first.

The repo has two parts:
- **Python simulation** (`main.py`, `src/`): the original planner, visualized with `matplotlib`.
- **Browser simulator** (`docs/index.html`): the same planner running in the browser, with editable settings, animation and an event log.

## Features
- **Robot Types**:
  - **Humanoid**: ground robot.
  - **Driver**: ground robot.
  - **Quadrotor**: aerial robot, flies in its own layer above the floor.
- **Grid Initialization**: creates an $N \times N$ grid from user input (3 to 10) with $2 \times N$ robots. Each robot gets a random type, start cell and goal cell.
- **Movement**:
  - Each step, a robot moves one cell toward its goal.
  - It closes the X gap first, then the Y gap.
- **Collision Handling**:
  - Ground robots are checked against ground robots, and aerial robots against aerial robots.
  - A conflict is two robots in the same layer planning to enter the same cell.
  - The robot closer to its goal (Euclidean distance) gets right of way; the other waits in place.
  - Ties are resolved randomly.
  - Robots that share the same goal are not checked against each other.
- **Visualization**: `matplotlib` plots each step, with dashed lines from every robot to its goal.

## Live Demo
Open **[robotwarehouse.dhruvpathak.com](https://robotwarehouse.dhruvpathak.com)**. No install needed.

- **Configure**: grid size (3 to 14), number of each robot type, and a seed to reproduce a layout.
- **Rules**: path order (X then Y, or Y then X), right of way (closer, farther or lower ID), tie-break (coin flip or lower ID), plus toggles for each collision-handling improvement.
- **Presets**:
  - **Repo rules** (default): match the Python code in `src/`.
  - **Safer rules**: re-check conflicts until none remain, keep waiting robots' cells reserved, detect head-on swaps, sidestep when blocked, and reroute around parked robots.
- **Playback**: autoplay or step forward and back one move at a time, scrub to any step, and change speed. Keyboard: `Space`, `←`, `→`.
- **Event log**: a terminal panel lists every move, each conflict detected (`DETECT`), how it was handled (`YIELD`, `SIDESTEP`, `REROUTE`, `DETOUR`), collisions the planner missed (`CRASH`), arrivals and `DEADLOCK`.

## Known Limitations of the Python Planner
The browser simulator's **Repo rules** reproduce these, so they can be seen step by step.
- **Deadlocks**: a robot parked on its goal has distance 0, so it always wins right of way. Any robot whose path crosses it waits forever, and `python3 main.py` never exits.
- **Single-pass checking**: each pair of robots is checked once per step. When a robot yields, it can create a new conflict with a pair already checked, and two robots end up in the same cell.
- **No swap detection**: two robots moving head-on trade cells and pass through each other.
- **Waiting robots can be overrun**: a robot standing still that loses on distance is told to wait, which changes nothing, so the other robot moves into its cell.

## Technical Information

### Design Principles
- **Object-Oriented Programming (OOP)**: each robot and the grid are objects, which keeps state management clean and extensible.
- **Modularity**: grid management, robot behavior and simulation control live in separate modules.

### Deployment
- GitHub Pages serves the `docs/` folder from the `main` branch.
- `docs/index.html` has no build step and no dependencies beyond Google Fonts. Edit the file and push to update the site.

## Running the Python Simulation

### Prerequisites
- Python 3.x
- `pip`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dhruvpathak1/Warehouse_Robot_Management_System_Design.git
   cd Warehouse_Robot_Management_System_Design
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. Run the simulation:
   ```bash
   python3 main.py
   ```
2. Enter the grid size $N$ when prompted (3 to 10).
3. A `matplotlib` window shows the current step. Close it to advance to the next step.
4. If robots deadlock, the loop keeps running. Press `Ctrl+C` in the terminal to stop.

---
---
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
