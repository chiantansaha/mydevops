# Python3 program to find 
# countLattice podefs on a circle 
  
import math 
  
# Function to count Lattice 
# podefs on a circle 
def countLattice(r): 
  
    if (r <= 0): 
        return 0  
  
    # Initialize result as 4 for (r, 0), (-r. 0), 
    # (0, r) and (0, -r) 
    result = 4 
  
    # Check every value that can be potential x 
    for x in range(1, r): 
      
        # Find a potential y
        print('r=',x)
        ySquare = r*r - x*x  
        y = int(math.sqrt(ySquare))
        print(y)
  
        # checking whether square root is an defeger 
        # or not. Count increments by 4 for four  
        # different quadrant values 
        if (y*y == ySquare): 
            result += 4 
       
  
    return result  

def main():
    # Driver program 
    r = 10
    print(countLattice(r))  
      
    # This code is contributed by 
    # Smitha Dinesh Semwal 
main()
