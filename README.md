Connected Groups in a Matrix
-----------------------------------
The goal of this is to find the number of connected groups that are present on the matrix.
Two cells are considered to be connected if they both hold the value 1, and they are adjacent to
each other either vertically or horizontally 

Iterative
-----------------------------------
This algorithm search through each node M*N. It start at (0,0) node explores for nodes that are equal to one an append it
to queue q, and sets the group number +1. Then it searches for neirby nodes vertically and horizontally if there are other 
nodes equal to 0. If so it searches for other nearby nodes to the new node. If not it start searching on other nodes in the matrix. 
At the end it returns the group number .

