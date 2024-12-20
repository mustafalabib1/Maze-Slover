from grid import *  # Import grid module (presumably handles the grid representation)
from colors import *  # Import color constants (e.g., ORANGE, YELLOW, etc.)
from search_algorithms import SearchAlgorithms  # Import base class for search algorithms
import math

class DepthLimitedSearch(SearchAlgorithms):
    """
    Implementation of Depth Limited Algorithm's algorithm for grid-based pathfinding.
    Colors:
    ORANGE -> Add to visit         = to_visit
    YELLOW -> Already visited      = visited
    GREEN  -> Path                 
    """
    # Define color states for visualization
    TO_VISIT = ORANGE
    VISITED = YELLOW

    def __init__(self, grid, window):
        """
        Initialize the algorithm with the grid, window for visualization, and delay for animation.
        """
        super().__init__(grid, window)
        self.to_visit = []  # Open list to keep track of cells to visit
        self.maxdepth= len(grid.linear_grid)

    def search(self): 
        """
        Execute Depth Limited algorithm to find the shortest path from origin to goal.
        """
        if not self.safe_to_start():  # Check if origin and goal are't set
            return "NO ORIGIN OR GOAL"
        
        i=1
        while i<=self.maxdepth:
            self.grid.delete_path()
            self.grid.draw_grid(self.window)
            pygame.display.update()
            pygame.time.delay(self.grid.delay)
                
            current_cell = self.grid.origin  # Start at the origin cell
            self.to_visit.append((1,current_cell))  # Add origin to to-visit list
        
            while len(self.to_visit) != 0:  # While there are cells to visit
                depth,current_cell = self.to_visit.pop()  
                
                # Mark current cell as visited
                self.update_color_state(current_cell, self.VISITED)                

                if current_cell == self.grid.goal:  # If the goal is reached
                    self.get_path()  # Trace the path from goal to origin
                    return
                
                if depth == i:
                    continue
                
                else:
                    for cell in self.grid.neighbors(current_cell):  # append each neighbor
                        cell.parent=current_cell
                        self.to_visit.append((depth+1,cell))
                        self.update_color_state(cell, self.TO_VISIT)
                        
                        
                    
            i*=2

        return "PATH NOT FOUND"