import sys
from src.grid import WarehouseGrid
from src.simulation import Simulation

def main():
    print("=== Warehouse Robot Management System ===")

    try:
        user_input = input("Enter value of N to make a NxN Grid (between 3 and 10): ")
        n = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        sys.exit(1)

    if not (3 <= n <= 10):
        print("Please enter a value between 3 and 10.")
        sys.exit(1)

    # Initialize grid and simulation
    grid_manager = WarehouseGrid(n)
    sim = Simulation(n, grid_manager)

    # Run the simulation
    try:
        sim.run()
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")

if __name__ == "__main__":
    main()
