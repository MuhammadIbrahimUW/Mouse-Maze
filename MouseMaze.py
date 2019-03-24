import random

def find_cheese_1(grid,row,column):
    '''
    searchs a grid for a 'C' using the row and column to guide a mouse 
    represented by an 'X' in the grid and returns True if the mouse can reach
    the cheese and False otherwise
    
    prints a new grid with 'X' where the mouse travels
    
    find_cheese_1: (Listof (Listof Str)) Nat Nat -> Bool
    
    effects: mututates the grid to contain 'X' where the mouse travels to find
    the cheese
    '''
    
    if grid[row][column] == 'C':
        flatten = list(map(lambda line: "".join(line),grid))
        print('\n'.join(flatten)) 
        return True
    
    elif grid[row].count('X') == 0:
        grid[row][column] = 'X'
        return find_cheese_1(grid, row, column)

    elif grid[row+1][column] == ' ' and grid[row+2][column] in ' C':
        grid[row][column] = 'X'
        return find_cheese_1(grid, row+2, column)

    elif grid[row][column-1] == ' ' and grid[row][column-2] in ' C':
        grid[row][column] = 'X'
        return find_cheese_1(grid, row, column-2)

    elif grid[row][column+1] == ' ' and grid[row][column+2] in ' C':
        grid[row][column+1] = 'X'
        return find_cheese_1(grid, row, column+2)

    elif grid[row-1][column] == ' ' and grid[row-2][column] in ' C':
        grid[row][column] = 'X'
        return find_cheese_1(grid, row-2, column)
    
    elif grid[row+2][column] == 'X':
        return find_cheese_1(grid,row+2,column)
    
    elif grid[row][column-2] == 'X':
        return find_cheese_1(grid,row,column-2)    
    
    elif grid[row][column+2] == 'X':
        return find_cheese_1(grid,row,column+2)  

    elif grid[row-2][column] == 'X':
        return find_cheese_1(grid,row-2,column)  
    
    else:
        flatten = list(map(lambda line: "".join(line),grid))
        print('\n'.join(flatten)) 
        return False

def find_cheese(grid):
    '''
    returns True if a mouse is able to find the cheese in a Grid and False
    otherwise
    
    prints a new grid with 'X' where the mouse travels
    
    find_cheese: (Listof (Listof Str)) => Bool
    
    effects: mututates the grid to contain 'X' where the mouse travels to find
    the cheese
    '''
    
    return find_cheese_1(grid, 1, grid[0].index(' '))



def build_grid(h,w,p):
    '''
    THIS CODE WAS GIVEN TO ME BY THE INSTRUCTORS IN CS116 WINTER 2019, I don't
    take credit for this only the above code was written by me.
    
    returns a randomized h by w grid of cells. The probability that any interior 
    wall is removed is given by p.
    
    Effects:
    prints the final grid to the screen
    
    build_grid: Nat Nat Float -> (listof (listof Str))
    requires: 0 <= p <= 1
              h > 0
              w > 0


    Example:
    build_grid(2,3,0.5) will print something similar to
    +-+ +-+
    | |   |
    + + +-+
    |   |C|
    +-+-+-+
    and return the corresponding list of lists.
    '''
    horz = "+-"*w + "+"
    vert = "| "*w + "|"
    grd = []
    for i in range(h):
        grd.append(list(horz))
        grd.append(list(vert))
    grd.append(list(horz)) 
    
    def get_wall_prob(p):
        '''
        returns a 0 or 1 based on the probability p. 0 is meant to indicate
        that the wall should be removed. 1 means it should stay. The parameter p
        represents a "desire for removal" (higher p means the wall is more likely 
        to be removed, i.e. return a 0).
        
        get_wall_prob: Float -> (anyof 0 1)
        requires: 0 <= p <= 1
        '''
        
        def random_dist(l):
            r = random.uniform(0, 1)
            cm = 0
            for num, prob in l:
                cm += prob
                if cm >= r:
                    return num
            return num     
        
        return random_dist([(0,p),(1,1-p)])
        
    # remove vertical walls based on p
    for i in range(h):
        y = 2*i + 1
        for j in range(w-1):
            x = 2*j + 2
            if get_wall_prob(p) == 0:
                grd[y][x] = ' '
                
    # remove horizontal walls based on p
    for i in range(h-1):
        y = 2*i + 2
        for j in range(w):
            x = 2*j + 1
            if get_wall_prob(p) == 0:
                grd[y][x] = ' '   

    # create entrance
    entrance = random.randrange(2*w)
                           
    while grd[0][entrance] != '-':
        entrance = random.randrange(2*w)
                           
    grd[0][entrance] = ' '
                                                
    # create cheese
    cheese_pos = 2*random.randrange(w)+1
                   
    while grd[-2][cheese_pos] == '|':
        cheese_pos = 2*random.randrange(w)+1
                           
    grd[-2][cheese_pos] = 'C'   
                
    # display grid
    flatten = list(map(lambda line: "".join(line),grd))
    print('\n'.join(flatten))    

    return grd