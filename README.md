### Rapidly-exploring Random Trees (RRT)
 This code contains the implementation of the Rapidly exploring random tree(RRT) algorithm.

The following code requires networkx and matplotlib libraries.

1) Install matplotlib
```sh 
        $ pip install matplotlib 
```
2) Install networkx
```sh
        $ pip install networkx
```
This algorithm creates a path from the start point to the end point by constructing edges by using random points on the area.

The code requires the user to input goal and obstacles which then the code uses to output a plot consisting of the trees and final path.

The area is 500 by 500 in dimension

Enter the goal(x,y) and obstacle list[(x1,y1),(x2,y2)] when prompted.

The obstacles are marked by blue and the goal is marked by green in the plot.

