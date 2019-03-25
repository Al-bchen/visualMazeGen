# visualMazeGen
Visualization on different algorithms of maze generation

## Environment for building
#### Windows / Mac
- Python 3.6.8
- PyQt 5.12
#### Linux(Ubuntu)
- Python 3.6.7
- PyQt 5.12.1


## Current Progress

### Generator
- Depth First Search / Recursive Backtracking
- Minimum Spanning Tree
  - Kruskal's Algorithm (same edge weight)
  - Prim's Algorithm (same edge weight)
- Hunt And Kill
- Recursive Division

### Solver
On progress...

### Program Design
Watch generation step by step

## Future Plan

### Base
- Migrate to Python 3.6.8 and PyQt 5.12.1 and test everything

### Generator
- None

###### Generator that is not going to be implemeted first
>Kruskal's Algorithm (random edge weight)  
>Prim's Algorithm (random edge weight)  
>Eller's Algorithm  
>Aldous-Broder Algorithm  
>Wilson's Algorithm  
>Binary Tree Algorithm  
>Growing Tree  
>Growing Forest

### Parallel Generator
- Depth First Search / Recursive Backtracking

### Solver
- Depth First Search
- Breath First Search
- Dijkstra Algorithm
  > This is almost the same as Breath First Search as the weights of edge are the same
- A* (A star) Algorithm

### Program Design
- Only update the display of the updated part, instead of repaint all graph
  - Improve display effect

## Known Bug
None 

## References

https://www.jamisbuck.org/mazes/  
http://www.astrolog.org/labyrnth/algrithm.htm
