# Warehouse Robot Management System

## Project Overview
This project simulates an efficient management system for multiple types of robots navigating a warehouse grid. The system ensures that robots reach their destinations while avoiding collisions, using prioritized movement strategies.

## Features
- **Robot Types**:
  - **Humanoid**: Ground-based robot.
  - **Driver**: Ground-based robot.
  - **Quadrotor**: Aerial-based robot.
- **Dynamic Grid Initialization**: Creates an $N \times N$ grid based on user input (between 3 and 10), with $2 \times N$ robots randomly placed.
- **Prioritized Movement**:
  - Robots move horizontally (X-axis) first, then vertically (Y-axis).
  - Shortest paths are determined using Euclidean distance.
- **Collision Avoidance**:
  - Ground-based robots avoid collisions with each other.
  - Aerial-based robots avoid collisions with each other.
  - Priorities are given to robots closer to their destinations.
  - Ties are resolved randomly.
- **Visualization**: Real-time plotting of robot movements using `matplotlib`.

## Technical Information

### Project Structure
```text
.
├── assets/             # Documentation assets and images
├── src/                # Source code
│   ├── grid.py         # Grid management and visualization logic
│   ├── robot.py        # Robot classes and property definitions
│   └── simulation.py   # Movement logic and collision resolution
├── main.py             # Application entry point
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

### Design Principles
- **Object-Oriented Programming (OOP)**: Each robot and the grid itself are represented as objects, allowing for cleaner state management and extensibility.
- **Modularity**: Logic is separated into distinct modules for grid management, robot behavior, and simulation control.

## Dependencies & Installation

### Prerequisites
- Python 3.x
- `pip` (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd warehouse-robot-management
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions

1. Run the simulation:
   ```bash
   python3 main.py
   ```
2. Enter the grid size $N$ when prompted (between 3 and 10).
3. Observe the `matplotlib` window for the step-by-step movement of robots. Close the plot window to proceed to the next simulation step.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
