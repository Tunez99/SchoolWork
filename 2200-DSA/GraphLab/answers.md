# CITS2200 Lab 6: Tranes and Planes, Security Routing
## Question 1 (3 marks)
Implement your solution by filling out the method stub in `trains_planes.py`.
Your implementation must pass the tests given in `test_trains_planes.py`, which can be invoked by running `python -m unittest test_trains_planes`.

See `trains_planes.py`.


## Question 2 (1 mark)
Give an argument for the correctness of your `trains_planes()` function.

YOUR ANSWER HERE
The algorithm processes all trains and flights in chronological order by sorting both lists by date.

To represent the problem we can use a Disjoint Set Union (DSU), where each tree within the forest, represents a set of interconnected cities. Using only trains that are available, we maintain their connectivity through a DSU . Unlike the Kruskals Algorithm, we don't require a priority queue or additional partition structure because all events happen in order by time. 

We increment over each flight and add any train that has become available before the flight date. Each train connects 2 cities and we merge components when a new train connection allows connectivity between different networks. This ensures at any point, the DSU correctly represents the set of cities that have connectivity via rail lines at that time.

For each flight, we check if both the source and destination exist in the same railway network by comparing each cities representative city. If they are the same, then some route exists via trains that can connect them and the flight can be replaced. 

Therefore, the properties of DSU allows us to correctly identify all flights for which a valid rail route exists at the time of departure. 

## Question 3 (1 mark)
Give an argument for the complexity of your `trains_planes()` function.

YOUR ANSWER HERE
The program has a few steps involved, firstly we sort both lists
trains sorted O(nlog(n))
planes sorted O(nlog(n))

The program uses a Disjoint Set Union data structure with path compression and union by rank. It's complexity is based on the inverse Ackermann function a(n)

find(u)                                 -> O(a(n)) 
union(A,B)                              -> O(a(n))
UnionFind Operations over all elements  -> O(n a(n))
Space complexity                        -> O(n)

Each train and flight is processed once, so the total number of DSU operations is linear in n. Therefore the overall complexity is O(nlog(n) + n a(n)), which simply becomes O(nlog(n)). Satisfying the target complexity.


## Question 1 (3 marks)
Implement your solution by filling out the method stub in `security_routing.py`.
Your implementation must pass the tests given in `test_security_routing.py`, which can be invoked by running `python -m unittest test_security_routing`.

See `security_routing.py`.


## Question 2 (1 mark)
Give an argument for the correctness of your `security_route()` function.

YOUR ANSWER HERE
To represent the problem we can visualise the paths as a graph, where each 'room' is a verticie, and the time taken to move to the next room are the edges weighted by time. We also note that the edges are mono-directional. 

To implement this, we first build a graph, from the list of stations we initialise the verticies and add their properties; a set of (directions, weigh, clearance requirements). This allows us to correctly model the graph structure.

We then implement Dijkstra's algorithm to solve the graph for the source to the destination.

To do this we implement a built-in python module "heapq" this allows us to create a priority queue that can return the state with the shortest current time.

The algorithm works in the following repetition: 
    - Find the shortest path currently available in the priority queue and pop it.
    - Every new path discovered after processing a state cannot be better than the current best candidate due to priority queue properties.
    - We check if a shorter time already exists, and skip that state.
    - We update the clearance, to create a new possible state and add to the queue. 
    - We add all new verticies with correct properties to the queue.
    - Once the target is popped, we have found the shortest path.

This algorithm guarantees we find the shortest route to each vertice with varying clearance states due to the properties of Dijkstra's algorithm, therefore proving correctness. 

## Question 3 (1 mark)
Give an argument for the complexity of your `security_route()` function.

YOUR ANSWER HERE
The solution found has 3 main data structures and algorithms, the following relevent complexities are as follow:
Note, we will be using arbritrary variables as follow:
V = verticies = len(stations)
E = edges     = len(segments)

Building the graph:
Due to the graph being in the form of an adjacency list.
Time complexity             -> O(N), where N = V+E
Space complexity            -> O(N), where N = V+E

Priority heap:
Inserting an element        -> O(log(n)) 
Pop/Extract                 -> O(log(n)) 

Dijkstra's algorithm: 
Dijkstra's algorithm is applied over an expanded state of (vertex, clearance) states, which has a constant factor of the input size. Each state is processed once and each edge is relaxed a constant number of times. Using a heap, operations cost O(log(n)) as seen before. This gives us the following:

Time comlexity              -> O((E*C + V*C)log(V))
Where C = constant factor, (Clearance states)
E is our edges and V is vertecies.

-> O(C(E + V)log(V))
-> O(Nlog(N)), where N = E + V

Overall the dominant cost is Dijkstra's algorithm leaving us with a total time complexity of O(Nlog(N)) satisfying the target complexity.
