"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # we start creating a new list that contains all numbers passed in number_list, as long as they're not zero
    result = [element for element in line if element != 0]
   
    # using some logic, if a number in result is equal to its previos number, we add those two numbers
    for element in range(0, len(result) - 1):
        if result[element] == result[element + 1]:
            result[element] *= 2
            result[element + 1] = 0
        
    # we modify result so that it contains only numbers different from zero
    result = [element for element in result if element != 0]
    
    # to finish, we add as many zeros as needed to result, so that its length is the same as the original number_list
    while len(result) < len(line):
            result.append(0)
            
    # we return result        
    return result
    

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = []
        self._moves = {UP:    [(0, j) for j in range(self._grid_width)],
                       DOWN:  [(self._grid_height - 1, j) for j in range(self._grid_width)],
                       LEFT:  [(i, 0) for i in range(self._grid_height)],
                       RIGHT: [(i, self._grid_width - 1) for i in range(self._grid_height)]}
        
        self.reset()
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)]
                         for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        _str = ""
        for element in self._grid:
            _str += str(element) + "\n"
        return _str
            
    
    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        move = False
        initial_tiles = self._moves[direction]
        for tile in initial_tiles:
            tiles = []
            col = tile[0]
            row = tile[1]
            while col < self._grid_height and row < self._grid_width and col >= 0 and row >= 0:
                tiles.append(self.get_tile(col, row))
                col += OFFSETS[direction][0]
                row += OFFSETS[direction][1]
            new_tiles = merge(tiles)
            col = tile[0]
            row = tile[1]
            idx = 0
            while col < self._grid_height and row < self._grid_width and col >= 0 and row >= 0:
                if self.get_tile(col, row)!= new_tiles[idx]:
                    move = True
                self.set_tile(col, row, new_tiles[idx])
                col += OFFSETS[direction][0]
                row += OFFSETS[direction][1]
                idx += 1
        if move:
            self.new_tile()
       
    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        random_choice = random.randrange(0, 10)
        pos = [random.randrange(0, self._grid_height), random.randrange(0, self._grid_width)]
       
        if random_choice == 4:
              value = 4
        else:
              value = 2
                
        if self.get_tile(pos[0], pos[1]) == 0:
            self.set_tile(pos[0], pos[1], value)
        else:
            self.new_tile()
      
    
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value
        
        
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]
    

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

