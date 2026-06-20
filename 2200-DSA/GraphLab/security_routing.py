
from enum import IntEnum
import heapq

class Clearance(IntEnum):
    NONE = 0
    RED = 1
    BLUE = 2
    GREEN = 3


def security_route(stations, segments, source, target):
    """Finds the fastest route from source station to target station.

    You start with no security clearance.
    When at a security station, you may choose to set your clearance to the same
    as that of the station.
    Each segment gives how long it takes to get from one station to another, and
    what clearance is required to be able to take that segment.

    Target Complexity: O(N lg N) in the size of the input (stations + segments).

    Args:
        stations: A list of what clearance is available at each station, or
            `NONE` if that station can not grant any clearance.
        segments: A list of `(u, v, t, c)` tuples, each representing a segment
            from `stations[u]` to `stations[v]` taking time `t` and requiring
            clearance `c` (`c` may be `NONE` if no clearance is required).
        source: The index of the station from which we start.
        target: The index of the station we are trying to reach.

    Returns:
        The minimum length of time required to get from `source` to `target`, or
        `None` if no route exists.
    """
    graph = Graph(stations, segments)
    solver = SecuritySolver(graph)
    
    return solver.solve(source, target)
    
    
class Graph:
    """
    Creates a graph object 
    This is a list of each out going route
    Location 0:
    Node[0] = (Door direction, Time taken, Clearance requirement)
    """
    def __init__(self, stations, segments):
        self.n = len(stations)          # Number of nodes
        self.stations = stations        # Node meta data

        # Initialise list for size of stations
        self.nodes = [[] for _ in range(self.n)]
        
        # Attach direction to location nodes
        for u, v, t, c in segments:
            self.nodes[u].append((v, t, c))


class State:
    """
    Creates a state object to track states
    Tracks:
        the current location
        the current clearance
        the current time
    """
    def __init__(self, node, clearance, time):
        self.node = node
        self.clearance = clearance
        self.time = time

    # Tells us how to compare objects -> time of each state
    def __lt__(self, other):
        return self.time < other.time
  
    
class SecuritySolver:
    """
        Used to solve a graph using Dijkstras Algorithm
    """
    def __init__(self, graph):
        self.graph = graph

    def solve(self, source, target):
        
        # Create starting state 
        # Stores all possible states to explore
        # Create a priority queue
        pq = []
        heapq.heappush(pq, State(source, Clearance.NONE, 0))
       
        # Best known time to reach a vertice
        dist = {}

        # While different states exist
        while pq:
            
            # Get the vertice with smallest total time for processing
            current = heapq.heappop(pq)
            u = current.node
            clr = current.clearance 
            time = current.time

            # Check if state has already been finalised
            if (u, clr) in dist:
                continue
            
            # Once vertice becomes smallest, finalise shortest route
            dist[(u, clr)] = time

            # Return if target is reached
            if u == target:
                return time

            # Get current stations clearance
            station_clr = self.graph.stations[u]
            
            # If the station has a change of clearance
            # Add new state with updated clearance
            if station_clr != Clearance.NONE and station_clr != clr:
                heapq.heappush(pq, State(u, station_clr, time))

            # Traverse Edges of current location
            # Attempt to move, if we have correct clearance
            # Push new states onto the heap for each edge
            for v, t, req in self.graph.nodes[u]:
                if req == Clearance.NONE or req == clr:
                    heapq.heappush(pq, State(v, clr, time + t))
        
        return None