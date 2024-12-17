from math import sqrt
from grid import *
from colors import *
from search_algorithms import SearchAlgorithms
from queue import PriorityQueue 

class AStar(SearchAlgorithms):
    # Define color states for visualization
    TO_VISIT = ORANGE
    VISITED = YELLOW
    def __init__(self, grid, window, delay=10):
        """
        Initialize the algorithm with the grid, window for visualization, and delay for animation.
        """
        super().__init__(grid, window, delay=delay)
        self.to_visit = PriorityQueue() # Open Priority Queue to keep track of cells to visit
       
    def manhattan_distance(self, cell):
        d = abs(cell.row - self.grid.goal.row) + abs(cell.col - self.grid.goal.col)
        return d

    def euclidian_distance(self, cell):
        d = int(sqrt(abs(cell.row - self.grid.goal.row)**2 + abs(cell.col - self.grid.goal.col)**2))
        return d

    def chebyshev_distance(self, cell):
        d = abs(cell.row - self.grid.goal.row)
        return d

    def search(self, heuristic): 
        if not self.safe_to_start(): 
            return "NO ORIGIN OR GOAL"
        
        current_cell = self.grid.origin  # Start at the origin cell
        self.to_visit.put((0,0,current_cell))  # Add origin to to-visit PriorityQueue
        
        while not self.to_visit.empty():  # While there are cells to visit
            h,cost, current_cell = self.to_visit.get()  
            # Mark current cell as visited
            self.update_color_state(current_cell, self.VISITED)                

            if current_cell == self.grid.goal:  # If the goal is reached
                self.get_path()  # Trace the path from goal to origin
                return
            else:
                for cell in self.grid.neighbors(current_cell):  # append each neighbor
                    NewCost=cost+1
                    cell.parent=current_cell
                    self.update_color_state(cell, self.TO_VISIT)
                    self.to_visit.put((NewCost+heuristic(cell),NewCost,cell))

        return "PATH NOT FOUND"
            