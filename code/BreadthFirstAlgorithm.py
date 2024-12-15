from grid import *  # Import grid module (presumably handles the grid representation)
from colors import *  # Import color constants (e.g., ORANGE, YELLOW, etc.)
from search_algorithms import SearchAlgorithms  # Import base class for search algorithms

class BreadthFirstAlgorithm(SearchAlgorithms):
    """
    Implementation of Dijkstra's algorithm for grid-based pathfinding.
    Colors:
    ORANGE -> Add to visit         = to_visit
    YELLOW -> Already visited      = visited
    GREEN  -> Path                 
    """
    # Define color states for visualization
    TO_VISIT = ORANGE
    VISITED = YELLOW
    
    def __init__(self, grid, window, delay=10):
        """
        Initialize the algorithm with the grid, window for visualization, and delay for animation.
        """
        super().__init__(grid, window, delay=delay)
        self.to_visit = []  # Open list to keep track of cells to visit

    def search(self): 
        """
        Execute Dijkstra's algorithm to find the shortest path from origin to goal.
        """
        if not self.safe_to_start():  # Check if origin and goal are't set
            return "NO ORIGIN OR GOAL"
        
        current_cell = self.grid.origin  # Start at the origin cell
        self.to_visit.append(current_cell)  # Add origin to to-visit list
        
        while len(self.to_visit) != 0:  # While there are cells to visit
            current_cell = self.to_visit.pop(0)  
            # Mark current cell as visited
            self.update_color_state(current_cell, self.VISITED)                

            if current_cell == self.grid.goal:  # If the goal is reached
                self.get_path()  # Trace the path from goal to origin
                return
            else:
                for cell in self.grid.neighbors(current_cell):  # append each neighbor
                    cell.parent=current_cell
                    self.update_color_state(cell, self.TO_VISIT)
                    self.to_visit.append(cell)
                    
        return "PATH NOT FOUND"

